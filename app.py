from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from resume_parser import extract_text
from skill_extractor import extract_skills
from ats_score import calculate_ats
from missing_skills import get_missing_skills
from jd_matcher import calculate_match
from suggestions import generate_suggestions
from section_analyzer import analyze_sections
from report_generator import generate_report
from chart_generator import generate_skill_chart


from database import (
    create_database,
    save_report,
    get_reports
)

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if not file:
        return "No file uploaded"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Extract Resume Text
    resume_text = extract_text(filepath)

    # Get Job Description
    job_description = request.form.get(
        "job_description",
        ""
    )

    # DEBUG
    print("\n========================")
    print("JOB DESCRIPTION:")
    print(job_description)
    print("========================\n")

    # Extract Skills
    skills = extract_skills(
        resume_text
    )

    print("RESUME SKILLS:")
    print(skills)

    # ATS Score
    ats_score = calculate_ats(
        resume_text,
        skills
    )

    # Missing Skills
    missing_skills = get_missing_skills(
        skills
    )

    # JD Match
    match_score = calculate_match(
        resume_text,
        job_description
    )

    print("JD MATCH SCORE:")
    print(match_score)

    # Suggestions
    suggestions = generate_suggestions(
        missing_skills
    )

    # Resume Completeness
    sections, completeness = analyze_sections(
        resume_text
    )

    # Save Analysis
    save_report(
        file.filename,
        ats_score,
        match_score
    )

    # Generate PDF
    report_path = os.path.join(
        REPORT_FOLDER,
        "ATS_Report.pdf"
    )

    generate_report(
        report_path,
        ats_score,
        match_score,
        skills,
        missing_skills,
        suggestions
    )

    return render_template(
        "result.html",
        ats_score=ats_score,
        match_score=match_score,
        skills=skills,
        missing_skills=missing_skills,
        suggestions=suggestions,
        sections=sections,
        completeness=completeness
    )


@app.route("/history")
def history():

    reports = get_reports()

    return render_template(
        "history.html",
        reports=reports
    )


@app.route("/download-report")
def download_report():

    report_path = os.path.join(
        REPORT_FOLDER,
        "ATS_Report.pdf"
    )

    if os.path.exists(
        report_path
    ):
        return send_file(
            report_path,
            as_attachment=True
        )

    return "PDF Report Not Found"


if __name__ == "__main__":

    os.makedirs(
        UPLOAD_FOLDER,
        exist_ok=True
    )

    os.makedirs(
        REPORT_FOLDER,
        exist_ok=True
    )

    create_database()

    app.run(
        debug=True
    )
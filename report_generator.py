from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import os


def generate_report(
    filename,
    ats_score,
    match_score,
    skills,
    missing_skills,
    suggestions
):

    # Create reports folder if it doesn't exist
    os.makedirs(
        os.path.dirname(filename),
        exist_ok=True
    )

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    # Title

    content.append(
        Paragraph(
            "AI Resume Analyzer Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # Scores

    content.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats_score}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>JD Match:</b> {match_score}%",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # Skills

    content.append(
        Paragraph(
            "Detected Skills",
            styles["Heading2"]
        )
    )

    for skill in skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 20)
    )

    # Missing Skills

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    for skill in missing_skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 20)
    )

    # Suggestions

    content.append(
        Paragraph(
            "Suggestions",
            styles["Heading2"]
        )
    )

    for suggestion in suggestions:

        content.append(
            Paragraph(
                f"• {suggestion}",
                styles["Normal"]
            )
        )

    pdf.build(content)

    print(
        f"PDF Generated Successfully: {filename}"
    )
def calculate_match(resume_text, job_description):

    if not job_description.strip():
        return 0

    skills_list = [
        "java", "python", "sql", "mysql",
        "mongodb", "html", "css", "javascript",
        "react", "node.js", "express.js",
        "git", "github", "linux",
        "docker", "kubernetes", "aws",
        "machine learning", "pandas",
        "numpy", "scikit-learn",
        "power bi", "tableau"
    ]

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    jd_skills = []
    matched_skills = []

    for skill in skills_list:

        if skill in job_description:
            jd_skills.append(skill)

            if skill in resume_text:
                matched_skills.append(skill)

    print("JD Skills:", jd_skills)
    print("Matched Skills:", matched_skills)

    if len(jd_skills) == 0:
        return 0

    score = (
        len(matched_skills) /
        len(jd_skills)
    ) * 100

    return round(score, 2)
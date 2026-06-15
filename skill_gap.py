def analyze_skill_gap(
    resume_text,
    job_description
):

    skills_list = [
        "java",
        "python",
        "sql",
        "mysql",
        "mongodb",
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "express.js",
        "git",
        "github",
        "linux",
        "docker",
        "kubernetes",
        "aws",
        "power bi",
        "tableau"
    ]

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched = []
    missing = []

    for skill in skills_list:

        if skill in job_description:

            if skill in resume_text:
                matched.append(skill)
            else:
                missing.append(skill)

    return matched, missing
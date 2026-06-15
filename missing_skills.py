def get_missing_skills(found_skills):

    required_skills = [
        "AWS",
        "Docker",
        "Kubernetes",
        "Power BI",
        "Tableau",
        "Git",
        "Linux",
        "Python",
        "SQL"
    ]

    missing = []

    for skill in required_skills:

        if skill not in found_skills:
            missing.append(skill)

    return missing
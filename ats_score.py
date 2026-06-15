def calculate_ats(text, skills):

    score = 0

    text = text.lower()

    # Skills Score (max 60)
    skill_score = len(skills) * 3
    score += min(skill_score, 60)

    # Important Fresher Sections
    if "education" in text:
        score += 10

    if "project" in text:
        score += 10

    if "certification" in text:
        score += 10

    if "technical skills" in text:
        score += 10

    # Experience is optional for freshers
    if "experience" in text:
        score += 5

    return min(score, 100)
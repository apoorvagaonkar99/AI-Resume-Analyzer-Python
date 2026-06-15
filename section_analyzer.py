def analyze_sections(text):

    text = text.lower()

    sections = {
        "Education": "education" in text,
        "Projects": "project" in text,
        "Certification": "certification" in text,
        "Skills": "technical skills" in text
    }

    present_sections = sum(sections.values())
    total_sections = len(sections)

    completeness = (present_sections / total_sections) * 100

    return sections, round(completeness, 2)
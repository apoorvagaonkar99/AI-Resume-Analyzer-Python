import pandas as pd

def extract_skills(text):

    skills_df = pd.read_csv("skills.csv")

    skills = skills_df["Skill"].tolist()

    found_skills = []

    text = text.lower()

    for skill in skills:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills
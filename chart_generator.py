import matplotlib.pyplot as plt
import os

def generate_skill_chart(matched, missing):

    os.makedirs("static", exist_ok=True)

    labels = ["Matched Skills", "Missing Skills"]

    values = [matched, missing]

    plt.figure(figsize=(5, 5))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Skill Match Analysis")

    plt.savefig("static/skill_chart.png")

    plt.close()
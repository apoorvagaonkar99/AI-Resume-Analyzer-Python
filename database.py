import sqlite3


def create_database():

    conn = sqlite3.connect(
        "resume_analysis.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS reports(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            ats_score INTEGER,
            match_score REAL
        )
        """
    )

    conn.commit()
    conn.close()


def save_report(
    filename,
    ats_score,
    match_score
):

    conn = sqlite3.connect(
        "resume_analysis.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reports(
            filename,
            ats_score,
            match_score
        )
        VALUES (?, ?, ?)
        """,
        (
            filename,
            ats_score,
            match_score
        )
    )

    conn.commit()
    conn.close()


def get_reports():

    conn = sqlite3.connect(
        "resume_analysis.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM reports
        ORDER BY id DESC
        """
    )

    reports = cursor.fetchall()

    conn.close()

    return reports
# ==========================================================
# STUDENT DATA GENERATOR
# ==========================================================

import random

import pandas as pd


def generate_student_data(rows):

    genders = ["Male", "Female"]

    departments = [
        "Statistics",
        "Computer Science",
        "Mathematics",
        "Economics",
        "Physics",
    ]

    records = []

    for i in range(1, rows + 1):

        attendance = random.randint(50, 100)

        study_hours = round(random.uniform(1, 10), 1)

        assignment_score = random.randint(40, 100)

        # Exam score is influenced partly by study hours
        # and attendance to make the dataset more realistic.
        exam_score = (
            assignment_score * 0.3
            + study_hours * 4
            + attendance * 0.3
            + random.uniform(-10, 10)
        )

        # Keep score between 0 and 100
        exam_score = round(
            max(0, min(100, exam_score)), 0
        )

        # Determine result
        result = "Pass" if exam_score >= 45 else "Fail"

        records.append({
            "Student_ID": f"STU{i:06d}",
            "Gender": random.choice(genders),
            "Age": random.randint(16, 30),
            "Department": random.choice(departments),
            "Attendance_%": attendance,
            "Study_Hours": study_hours,
            "Assignment_Score": assignment_score,
            "Exam_Score": exam_score,
            "Result": result,
        })

    return pd.DataFrame(records)
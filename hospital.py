# ==========================================================
# HOSPITAL DATA GENERATOR
# ==========================================================

import random
from datetime import datetime, timedelta

import pandas as pd


def generate_hospital_data(rows):

    genders = ["Male", "Female"]

    diagnoses = [
        "Malaria",
        "Typhoid",
        "Hypertension",
        "Diabetes",
        "Asthma",
        "Pneumonia",
    ]

    treatments = [
        "Medication",
        "Observation",
        "Therapy",
    ]

    records = []

    for i in range(1, rows + 1):

        age = random.randint(1, 85)

        systolic = random.randint(90, 180)

        diastolic = random.randint(60, 120)

        bmi = round(random.uniform(18, 40), 1)

        diagnosis = random.choice(diagnoses)

        admission_date = (
            datetime.today()
            - timedelta(days=random.randint(0, 365))
        ).date()

        records.append({
            "Patient_ID": f"PAT{i:06d}",
            "Age": age,
            "Gender": random.choice(genders),
            "Systolic_BP": systolic,
            "Diastolic_BP": diastolic,
            "BMI": bmi,
            "Diagnosis": diagnosis,
            "Treatment": random.choice(treatments),
            "Treatment_Cost": random.randint(5000, 500000),
            "Admission_Date": admission_date,
        })

    return pd.DataFrame(records)
# ==========================================================
# EMPLOYEE DATA GENERATOR
# ==========================================================

import random

import pandas as pd


def generate_employee_data(rows):

    departments = [
        "Finance",
        "HR",
        "IT",
        "Marketing",
        "Sales",
        "Operations",
    ]

    records = []

    for i in range(1, rows + 1):

        experience = random.randint(0, 20)

        # Salary increases somewhat with experience
        salary = (
            80000
            + experience * 25000
            + random.randint(-10000, 50000)
        )

        performance = random.randint(1, 5)

        overtime = random.randint(0, 30)

        promotion = (
            "Yes"
            if experience >= 5 and performance >= 4
            else "No"
        )

        records.append({
            "Employee_ID": f"EMP_{i:06d}",
            "Age": random.randint(20, 60),
            "Department": random.choice(departments),
            "Years_Experience": experience,
            "Salary": max(50000, salary),
            "Performance_Rating": performance,
            "Overtime_Hours": overtime,
            "Promotion": promotion,
        })

    return pd.DataFrame(records)
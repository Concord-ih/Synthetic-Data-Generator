# ==========================================================
# FINANCE / LOAN DATA GENERATOR
# ==========================================================

import random

import pandas as pd


def generate_finance_data(rows):

    employment_types = [
        "Employed",
        "Self-employed",
        "Unemployed",
    ]

    loan_types = [
        "Personal",
        "Business",
        "Education",
        "Auto",
    ]

    records = []

    for i in range(1, rows + 1):

        income = random.randint(50000, 1000000)

        loan_amount = random.randint(50000, 2000000)

        credit_score = random.randint(300, 850)

        employment = random.choice(employment_types)

        # Simple rule to add risk based on financial characteristics.

        default_probability = 0.15

        if credit_score < 550:
            default_probability += 0.30

        if loan_amount > income * 3:
            default_probability += 0.25

        if employment == "Unemployed":
            default_probability += 0.20

        # Risks can stack, based on the rule above

        default = (
            "Yes"
            if random.random() < min(default_probability, 0.90)
            else "No"
        )

        records.append({
            "Customer_ID": f"CUS_{i:06d}",
            "Income": income,
            "Loan_Amount": loan_amount,
            "Credit_Score": credit_score,
            "Employment": employment,
            "Loan_Type": random.choice(loan_types),
            "Interest_Rate": round(
                random.uniform(5, 30), 2
            ),
            "Default": default,
        })

    return pd.DataFrame(records)
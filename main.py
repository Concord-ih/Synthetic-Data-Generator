# ==========================================================
# SYNTHETIC DATA GENERATOR
#
# Main program
# ==========================================================

import sys
from pathlib import Path

from config import DEFAULT_ROWS, OUTPUT_FOLDER
from sales import generate_sales_data
from hospital import generate_hospital_data
from student import generate_student_data
from employee import generate_employee_data
from finance import generate_finance_data


# Convert output folder into a Path object
OUTPUT_DIR = Path(OUTPUT_FOLDER)

# Create output folder if it doesn't exist
OUTPUT_DIR.mkdir(exist_ok=True)


def main():

    # ------------------------------------------------------
    # Ask the user which dataset they want
    # ------------------------------------------------------

    print("\nSynthetic Data Generator")
    print("-" * 30)

    print("1. Sales")
    print("2. Hospital")
    print("3. Student")
    print("4. Employee")
    print("5. Finance")

    choice = input("\nChoose dataset: ")

    # ------------------------------------------------------
    # Ask how many rows they want
    # ------------------------------------------------------

    rows_input = input(
        f"Number of rows (default {DEFAULT_ROWS}): "
    )

    # Use default if the user presses Enter
    rows = (
        DEFAULT_ROWS
        if rows_input.strip() == ""
        else int(rows_input)
    )

    # ------------------------------------------------------
    # Generate the selected dataset
    # ------------------------------------------------------

    if choice == "1":

        df = generate_sales_data(rows)
        filename = "sales.csv"

    elif choice == "2":

        df = generate_hospital_data(rows)
        filename = "hospital.csv"

    elif choice == "3":

        df = generate_student_data(rows)
        filename = "student.csv"

    elif choice == "4":

        df = generate_employee_data(rows)
        filename = "employee.csv"

    elif choice == "5":

        df = generate_finance_data(rows)
        filename = "finance.csv"

    else:

        print("Invalid choice.")
        return

    # ------------------------------------------------------
    # Save dataset
    # ------------------------------------------------------

    output_path = OUTPUT_DIR / filename

    df.to_csv(output_path, index=False)

    # ------------------------------------------------------
    # Display summary
    # ------------------------------------------------------

    print("\nDataset generated successfully!")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Saved to: {output_path}")


# Run the program
if __name__ == "__main__":
    main()
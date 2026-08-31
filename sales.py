# ==========================================================
# SALES DATA GENERATOR
# ==========================================================

import random
from datetime import datetime, timedelta

import pandas as pd


def generate_sales_data(rows):
    """
    Generate a synthetic sales dataset.

    Parameters:
        rows (int): Number of records to generate.

    Returns:
        pandas.DataFrame
    """

    # Product catalog.
    # The relationship between category, product and brand
    # prevents unrealistic combinations.
    product_catalog = {
        "Computers": {
            "Laptop": ["HP", "Dell", "Lenovo", "Apple"],
            "Desktop": ["HP", "Dell", "Lenovo"],
            "Monitor": ["Dell", "LG", "Samsung", "HP"],
        },

        "Mobile": {
            "Smartphone": ["Apple", "Samsung", "Xiaomi", "Tecno", "Infinix"],
            "Tablet": ["Apple", "Samsung", "Lenovo"],
            "Smartwatch": ["Apple", "Samsung", "Xiaomi"],
        },

        "Accessories": {
            "Keyboard": ["Logitech", "HP", "Dell"],
            "Mouse": ["Logitech", "HP", "Dell"],
            "Headphones": ["Sony", "JBL", "Samsung"],
            "Power Bank": ["Anker", "Oraimo", "Xiaomi"],
        },

        "Office Equipment": {
            "Printer": ["Canon", "Epson", "HP"],
        },
    }

    regions = [
        "Lagos",
        "Abuja",
        "Kano",
        "Ibadan",
        "Kaduna",
        "Osogbo",
        "Port Harcourt",
    ]

    payment_methods = [
        "Card",
        "Transfer",
        "Cash",
        "PayPal",
    ]

    records = []

    for i in range(1, rows + 1):

        # Select a category
        category = random.choice(list(product_catalog.keys()))

        # Select a product from that category
        product = random.choice(
            list(product_catalog[category].keys())
        )

        # Select a valid brand for that product
        brand = random.choice(
            product_catalog[category][product]
        )

        quantity = random.randint(1, 10)

        unit_price = random.randint(50, 2500)

        discount = random.choice([0, 5, 10, 15, 20])

        subtotal = quantity * unit_price

        discount_amount = subtotal * discount / 100

        total = subtotal - discount_amount

        # Generate a date within the last year
        order_date = (
            datetime.today()
            - timedelta(days=random.randint(0, 365))
        ).date()

        records.append({
            "Order_ID": f"ORD_{i:06d}",
            "Category": category,
            "Product": product,
            "Brand": brand,
            "Quantity": quantity,
            "Unit_Price": unit_price,
            "Discount_%": discount,
            "Subtotal": round(subtotal, 2),
            "Discount_Amount": round(discount_amount, 2),
            "Total_Amount": round(total, 2),
            "Region": random.choice(regions),
            "Payment_Method": random.choice(payment_methods),
            "Order_Date": order_date,
        })

    return pd.DataFrame(records)
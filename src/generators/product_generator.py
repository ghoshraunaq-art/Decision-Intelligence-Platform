from faker import Faker
import random

from src.database.db_connection import get_connection

fake = Faker()


def insert_products():
    conn = get_connection()
    cursor = conn.cursor()

    product_names = [
        "Smartphone",
        "Laptop",
        "Headphones",
        "Camera",
        "Smart TV",
        "Shoes",
        "Tablet",
        "Monitor",
        "Keyboard",
        "Mouse",
        "Smartwatch",
        "Printer",
        "Speaker",
        "Power Bank",
        "Router",
        "Microphone",
        "SSD",
        "Hard Drive",
        "Gaming Chair",
        "Webcam"
    ]

    for name in product_names:

        brand_id = random.randint(1, 20)
        category_id = random.randint(1, 10)

        cost_price = round(random.uniform(500, 50000), 2)

        selling_price = round(
            cost_price * random.uniform(1.10, 1.45),
            2
        )

        cursor.execute(
            """
            INSERT INTO products
            (
                product_name,
                brand_id,
                category_id,
                cost_price,
                selling_price
            )

            VALUES
            (%s,%s,%s,%s,%s)
            """,

            (
                name,
                brand_id,
                category_id,
                cost_price,
                selling_price
            )
        )

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Products inserted successfully.")


if __name__ == "__main__":
    insert_products()
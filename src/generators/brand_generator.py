from faker import Faker
import random
from src.database.db_connection import get_connection

fake = Faker()

brands = [
    "Apple",
    "Samsung",
    "Sony",
    "Dell",
    "HP",
    "Lenovo",
    "Asus",
    "Acer",
    "Nike",
    "Adidas",
    "Puma",
    "Boat",
    "JBL",
    "Canon",
    "Nikon",
    "LG",
    "OnePlus",
    "Xiaomi",
    "Philips",
    "Panasonic"
]


def insert_brands():
    conn = get_connection()
    cursor = conn.cursor()

    for brand in brands:
        cursor.execute(
            """
            INSERT INTO brands (brand_name)
            VALUES (%s)
            """,
            (brand,)
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Brands inserted successfully.")


if __name__ == "__main__":
    insert_brands()
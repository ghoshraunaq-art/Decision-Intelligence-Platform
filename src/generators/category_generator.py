from src.database.db_connection import get_connection

categories = [
    "Mobiles",
    "Laptops",
    "Televisions",
    "Headphones",
    "Cameras",
    "Shoes",
    "Clothing",
    "Accessories",
    "Gaming",
    "Kitchen"
]


def insert_categories():
    conn = get_connection()
    cursor = conn.cursor()

    for category in categories:
        cursor.execute(
            """
            INSERT INTO categories (category_name)
            VALUES (%s)
            """,
            (category,)
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Categories inserted successfully.")


if __name__ == "__main__":
    insert_categories()
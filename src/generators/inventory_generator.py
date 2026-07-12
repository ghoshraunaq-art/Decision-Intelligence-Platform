from faker import Faker
import random

from src.database.db_connection import get_connection

fake = Faker()


def insert_inventory():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT product_id, cost_price FROM products")
    products = cursor.fetchall()

    for product in products:

        product_id = product[0]
        purchase_price = product[1]

        stock_quantity = random.randint(20, 300)

        last_restock_date = fake.date_between(
            start_date="-180d",
            end_date="today"
        )

        cursor.execute(
            """
            INSERT INTO inventory
            (
                product_id,
                stock_quantity,
                purchase_price,
                last_restock_date
            )

            VALUES
            (%s,%s,%s,%s)
            """,

            (
                product_id,
                stock_quantity,
                purchase_price,
                last_restock_date
            )
        )

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Inventory inserted successfully.")


if __name__ == "__main__":
    insert_inventory()
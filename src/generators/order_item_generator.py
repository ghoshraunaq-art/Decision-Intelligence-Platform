import random

from src.database.db_connection import get_connection


def insert_order_items():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT order_id FROM orders")
    orders = cursor.fetchall()

    cursor.execute("SELECT product_id FROM products")
    products = cursor.fetchall()

    product_ids = [product[0] for product in products]

    for order in orders:

        order_id = order[0]

        items = random.randint(1, 5)

        selected_products = random.sample(
            product_ids,
            items
        )

        for product in selected_products:

            quantity = random.randint(1, 4)

            cursor.execute(
                """
                INSERT INTO order_items
                (
                    order_id,
                    product_id,
                    quantity
                )

                VALUES
                (%s,%s,%s)
                """,

                (
                    order_id,
                    product,
                    quantity
                )
            )

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Order Items inserted successfully.")


if __name__ == "__main__":
    insert_order_items()
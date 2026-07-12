from faker import Faker

from src.database.db_connection import get_connection

fake = Faker()


def insert_sales():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            oi.order_item_id,
            oi.quantity,
            p.selling_price

        FROM order_items oi

        JOIN products p

        ON oi.product_id = p.product_id
        """
    )

    order_items = cursor.fetchall()

    for item in order_items:

        order_item_id = item[0]
        quantity_sold = item[1]
        selling_price = item[2]

        sale_date = fake.date_between(
            start_date="-365d",
            end_date="today"
        )

        cursor.execute(
            """
            INSERT INTO sales
            (
                order_item_id,
                sale_date,
                quantity_sold,
                selling_price
            )

            VALUES
            (%s,%s,%s,%s)
            """,

            (
                order_item_id,
                sale_date,
                quantity_sold,
                selling_price
            )
        )

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Sales inserted successfully.")


if __name__ == "__main__":
    insert_sales()
from faker import Faker
import random

from src.database.db_connection import get_connection

fake = Faker()


payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]


def insert_orders():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT customer_id FROM customers")

    customers = cursor.fetchall()

    for customer in customers:

        customer_id = customer[0]

        number_of_orders = random.randint(1,4)

        for _ in range(number_of_orders):

            order_date = fake.date_between(
                start_date="-365d",
                end_date="today"
            )

            payment_method = random.choice(payment_methods)

            cursor.execute(
                """
                INSERT INTO orders
                (
                    customer_id,
                    order_date,
                    payment_method
                )

                VALUES
                (%s,%s,%s)
                """,

                (
                    customer_id,
                    order_date,
                    payment_method
                )
            )

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Orders inserted successfully.")


if __name__ == "__main__":
    insert_orders()
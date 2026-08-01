from faker import Faker
import random

from src.database.db_connection import get_connection

fake = Faker()

genders = ["Male", "Female"]


def insert_customers():

    conn = get_connection()
    cursor = conn.cursor()

    # Fetch every region dynamically
    cursor.execute("""
        SELECT region_id
        FROM regions
        ORDER BY region_id;
    """)

    region_ids = [row[0] for row in cursor.fetchall()]

    # Create 2 customers for every region
    for region_id in region_ids:

        for _ in range(2):

            gender = random.choice(genders)

            if gender == "Male":
                name = fake.name_male()
            else:
                name = fake.name_female()

            email = fake.unique.email()

            age = random.randint(20, 45)

            join_date = fake.date_between(
                start_date="-2y",
                end_date="today"
            )

            cursor.execute(
                """
                INSERT INTO customers
                (
                    customer_name,
                    email,
                    gender,
                    age,
                    join_date,
                    region_id
                )

                VALUES (%s,%s,%s,%s,%s,%s)
                """,
                (
                    name,
                    email,
                    gender,
                    age,
                    join_date,
                    region_id
                )
            )

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Customers inserted successfully!")


if __name__ == "__main__":
    insert_customers()
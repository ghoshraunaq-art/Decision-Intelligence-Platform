from src.database.db_connection import get_connection

countries = [
    "India",
    "United States",
    "Canada",
    "Germany",
    "United Kingdom",
    "Australia",
    "Japan",
    "France",
    "Brazil",
    "Singapore"
]

def insert_countries():
    connection = get_connection()
    cursor = connection.cursor()

    for country in countries:
        cursor.execute(
            """
            INSERT INTO countries (country_name)
            VALUES (%s);
            """,
            (country,)
        )

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    insert_countries()
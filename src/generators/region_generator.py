from src.database.db_connection import get_connection

regions = [
    "Alaska",
    "California",
    "Colorado",
    "Hawaii",
    "Iowa",
    "Kansas",
    "Louisiana",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "New Jersey",
    "Pennsylvania",
    "South Dakota",
    "Tennessee",
    "Washington"
]

def insert_regions():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT country_id FROM countries;")
    country_ids = [row[0] for row in cursor.fetchall()]

    for i, region in enumerate(regions):

        cursor.execute(
            """
            INSERT INTO regions
            (region_name, country_id)
            VALUES (%s,%s)
            """,
            (
                region,
                country_ids[i % len(country_ids)]
            )
        )

    connection.commit()

    cursor.close()
    connection.close()

    print("✅ Regions inserted successfully!")

if __name__ == "__main__":
    insert_regions()
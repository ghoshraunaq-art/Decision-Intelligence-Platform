from src.database.db_connection import get_connection

regions = {

    "United States": [
        "Alaska",
        "California",
        "Colorado",
        "Florida",
        "Georgia",
        "Hawaii",
        "Illinois",
        "Iowa",
        "Kansas",
        "Louisiana",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nevada",
        "New Jersey",
        "New York",
        "North Carolina",
        "Ohio",
        "Oregon",
        "Pennsylvania",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Virginia",
        "Washington",
        "Wisconsin"
    ],

    "Canada": [
        "Ontario",
        "Quebec",
        "British Columbia",
        "Alberta",
        "Manitoba",
        "Saskatchewan",
        "Nova Scotia",
        "New Brunswick"
    ],

    "Australia": [
        "New South Wales",
        "Victoria",
        "Queensland",
        "Western Australia",
        "South Australia",
        "Tasmania",
        "Northern Territory",
        "Australian Capital Territory"
    ],

    "Germany": [
        "Bavaria",
        "Berlin",
        "Hamburg",
        "Hesse",
        "Saxony",
        "Brandenburg",
        "Baden-Württemberg",
        "Lower Saxony"
    ],

    "United Kingdom": [
        "England",
        "Scotland",
        "Wales",
        "Northern Ireland",
        "Greater London",
        "Manchester",
        "Liverpool",
        "Birmingham"
    ],

    "India": [
        "Delhi",
        "Maharashtra",
        "Karnataka",
        "Tamil Nadu",
        "West Bengal",
        "Telangana",
        "Gujarat",
        "Rajasthan",
        "Uttar Pradesh",
        "Punjab",
        "Odisha",
        "Kerala"
    ],

    "Japan": [
        "Tokyo",
        "Osaka",
        "Kyoto",
        "Hokkaido",
        "Aichi",
        "Fukuoka",
        "Hiroshima",
        "Okinawa"
    ],

    "France": [
        "Île-de-France",
        "Normandy",
        "Brittany",
        "Occitanie",
        "Provence-Alpes-Côte d'Azur",
        "Nouvelle-Aquitaine",
        "Grand Est",
        "Auvergne-Rhône-Alpes"
    ],

    "Brazil": [
        "São Paulo",
        "Rio de Janeiro",
        "Bahia",
        "Paraná",
        "Minas Gerais",
        "Pernambuco",
        "Ceará",
        "Rio Grande do Sul"
    ],

    "Singapore": [
        "Central Region",
        "East Region",
        "North Region",
        "North-East Region",
        "West Region"
    ]
}


def insert_regions():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT country_id, country_name
        FROM countries;
    """)

    country_lookup = {
        name: cid
        for cid, name in cursor.fetchall()
    }

    for country, region_list in regions.items():

        country_id = country_lookup[country]

        for region in region_list:

            cursor.execute(
                """
                INSERT INTO regions
                (region_name, country_id)
                VALUES (%s, %s)
                """,
                (
                    region,
                    country_id
                )
            )

    connection.commit()

    cursor.close()
    connection.close()

    print("✅ Regions inserted successfully!")


if __name__ == "__main__":
    insert_regions()
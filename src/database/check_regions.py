from src.database.db_connection import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
SELECT
    c.country_name,
    r.region_name
FROM regions r
JOIN countries c
ON r.country_id = c.country_id
ORDER BY c.country_name, r.region_name;
""")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
from src.database.db_connection import get_connection

customers = [

    ("Rahul Sharma","rahul@gmail.com","Male",22,"2026-07-04",1),
    ("Priya Singh","priya@gmail.com","Female",21,"2026-07-04",2),
    ("John Smith","john@gmail.com","Male",30,"2026-07-04",3),
    ("Emma Watson","emma@gmail.com","Female",28,"2026-07-04",4),
    ("Akash Roy","akash@gmail.com","Male",24,"2026-07-04",5),
    ("Maria Garcia","maria@gmail.com","Female",29,"2026-07-04",6),
    ("David Lee","david@gmail.com","Male",35,"2026-07-04",7),
    ("Sophia Brown","sophia@gmail.com","Female",27,"2026-07-04",8),
    ("Arjun Das","arjun@gmail.com","Male",23,"2026-07-04",9),
    ("Kevin Miller","kevin@gmail.com","Male",31,"2026-07-04",10),

    ("Rohit Kumar","rohit@gmail.com","Male",26,"2026-07-04",11),
    ("Ananya Sen","ananya@gmail.com","Female",24,"2026-07-04",12),
    ("Chris Evans","chris@gmail.com","Male",33,"2026-07-04",13),
    ("Neha Kapoor","neha@gmail.com","Female",25,"2026-07-04",14),
    ("Michael Scott","michael@gmail.com","Male",40,"2026-07-04",15),
    ("Sarah Wilson","sarah@gmail.com","Female",29,"2026-07-04",16)

]


def insert_customers():
    connection = get_connection()
    cursor = connection.cursor()

    for customer in customers:
        cursor.execute(
            """
            INSERT INTO customers
            (customer_name, email, gender, age, join_date, region_id)
            VALUES (%s, %s, %s, %s, %s, %s);
            """,
            customer
        )

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    insert_customers()
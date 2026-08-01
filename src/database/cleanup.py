from src.database.db_connection import get_connection


def cleanup():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sales;")
    cursor.execute("DELETE FROM order_items;")
    cursor.execute("DELETE FROM orders;")
    cursor.execute("DELETE FROM customers;")
    cursor.execute("DELETE FROM regions;")

    cursor.execute(
        "ALTER SEQUENCE regions_region_id_seq RESTART WITH 1;"
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Database cleaned successfully")


if __name__ == "__main__":
    cleanup()
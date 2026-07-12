import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="decision_intelligence",
        user="postgres",
        password="rq2005",
        port="5432"
    )

    return connection

from database.db_connection import get_connection


def execute_query(query, params=None):

    conn = get_connection()
    cursor = conn.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def total_revenue(region="All"):

    query = """

        SELECT
            COALESCE(SUM(s.quantity_sold*s.selling_price),0)

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id=oi.order_item_id

        JOIN orders o
            ON oi.order_id=o.order_id

        JOIN customers c
            ON o.customer_id=c.customer_id

        JOIN regions r
            ON c.region_id=r.region_id

    """

    params=None

    if region!="All":
        query+="WHERE r.region_name=%s"
        params=(region,)

    return execute_query(query,params)[0][0]

def total_products_sold(region="All"):

    query="""

        SELECT
            COALESCE(SUM(s.quantity_sold),0)

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id=oi.order_item_id

        JOIN orders o
            ON oi.order_id=o.order_id

        JOIN customers c
            ON o.customer_id=c.customer_id

        JOIN regions r
            ON c.region_id=r.region_id

    """

    params=None

    if region!="All":
        query+="WHERE r.region_name=%s"
        params=(region,)

    return execute_query(query,params)[0][0]


def total_customers(region="All"):

    query="""

        SELECT
            COUNT(DISTINCT c.customer_id)

        FROM customers c

        JOIN regions r
            ON c.region_id=r.region_id

    """

    params=None

    if region!="All":
        query+="WHERE r.region_name=%s"
        params=(region,)

    return execute_query(query,params)[0][0]


def total_orders(region="All"):

    query="""

        SELECT
            COUNT(DISTINCT o.order_id)

        FROM orders o

        JOIN customers c
            ON o.customer_id=c.customer_id

        JOIN regions r
            ON c.region_id=r.region_id

    """

    params=None

    if region!="All":
        query+="WHERE r.region_name=%s"
        params=(region,)

    return execute_query(query,params)[0][0]
def revenue_by_category(region="All"):

    query = """
        SELECT
            c.category_name,
            SUM(s.quantity_sold * s.selling_price) AS revenue

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories c
            ON p.category_id = c.category_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers cu
            ON o.customer_id = cu.customer_id

        JOIN regions r
            ON cu.region_id = r.region_id
    """

    if region != "All":
        query += f"""
        WHERE r.region_name = '{region}'
        """

    query += """
        GROUP BY c.category_name
        ORDER BY revenue DESC;
    """

    return execute_query(query)

def revenue_by_region(region="All"):

    query = """

        SELECT
            r.region_name,
            SUM(s.quantity_sold * s.selling_price) AS revenue

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers cu
            ON o.customer_id = cu.customer_id

        JOIN regions r
            ON cu.region_id = r.region_id

    """

    if region != "All":
        query += f"""
        WHERE r.region_name = '{region}'
        """

    query += """

        GROUP BY r.region_name

        ORDER BY revenue DESC;

    """

    return execute_query(query)


def top_products():

    return execute_query("""

        SELECT
            p.product_name,
            SUM(s.quantity_sold) AS total_sold

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN products p
            ON oi.product_id = p.product_id

        GROUP BY p.product_name

        ORDER BY total_sold DESC

        LIMIT 10;

    """)


def top_customers():

    return execute_query("""

        SELECT
            c.customer_name,
            SUM(s.quantity_sold * s.selling_price) AS revenue

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers c
            ON o.customer_id = c.customer_id

        GROUP BY c.customer_name

        ORDER BY revenue DESC

        LIMIT 10;

    """)


def inventory_status():

    return execute_query("""

        SELECT
            p.product_name,
            i.stock_quantity

        FROM inventory i

        JOIN products p
            ON i.product_id = p.product_id

        ORDER BY i.stock_quantity ASC

        LIMIT 10;

    """)

def monthly_revenue():

    return execute_query("""

        SELECT
            TO_CHAR(sale_date,'Mon YYYY') AS month,
            SUM(quantity_sold*selling_price) AS revenue

        FROM sales

        GROUP BY
            DATE_TRUNC('month', sale_date),
            TO_CHAR(sale_date,'Mon YYYY')

        ORDER BY
            DATE_TRUNC('month', sale_date);

    """)


def category_sales():

    return execute_query("""

        SELECT
            c.category_name,
            SUM(s.quantity_sold)

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id=oi.order_item_id

        JOIN products p
            ON oi.product_id=p.product_id

        JOIN categories c
            ON p.category_id=c.category_id

        GROUP BY c.category_name

        ORDER BY 2 DESC;

    """)
def available_regions():

    return execute_query("""

        SELECT DISTINCT
            r.region_name

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers c
            ON o.customer_id = c.customer_id

        JOIN regions r
            ON c.region_id = r.region_id

        ORDER BY r.region_name;

    """)

def available_countries(region="All"):

    if region == "All":
        return execute_query("""
            SELECT DISTINCT
                c.country_name
            FROM countries c
            ORDER BY c.country_name
        """)

    return execute_query("""
        SELECT DISTINCT
            c.country_name
        FROM countries c
        JOIN regions r
            ON c.region_id = r.region_id
        WHERE r.region_name = %s
        ORDER BY c.country_name
    """, (region,))

def available_categories(region="All", country="All"):

    query = """
        SELECT DISTINCT
            cat.category_name
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN categories cat
            ON p.category_id = cat.category_id
        JOIN orders o
            ON oi.order_id = o.order_id
        JOIN customers cu
            ON o.customer_id = cu.customer_id
        JOIN countries c
            ON cu.country_id = c.country_id
        JOIN regions r
            ON c.region_id = r.region_id
        WHERE 1=1
    """

    params = []

    if region != "All":
        query += " AND r.region_name = %s"
        params.append(region)

    if country != "All":
        query += " AND c.country_name = %s"
        params.append(country)

    query += " ORDER BY cat.category_name"

    return execute_query(query, tuple(params))


def available_products(region="All", country="All", category="All"):

    query = """
        SELECT DISTINCT
            p.product_name
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN categories cat
            ON p.category_id = cat.category_id
        JOIN orders o
            ON oi.order_id = o.order_id
        JOIN customers cu
            ON o.customer_id = cu.customer_id
        JOIN countries c
            ON cu.country_id = c.country_id
        JOIN regions r
            ON c.region_id = r.region_id
        WHERE 1=1
    """

    params = []

    if region != "All":
        query += " AND r.region_name = %s"
        params.append(region)

    if country != "All":
        query += " AND c.country_name = %s"
        params.append(country)

    if category != "All":
        query += " AND cat.category_name = %s"
        params.append(category)

    query += " ORDER BY p.product_name"

    return execute_query(query, tuple(params))


def available_years():

    return execute_query("""
        SELECT DISTINCT
            EXTRACT(YEAR FROM order_date)
        FROM orders
        ORDER BY 1
    """)
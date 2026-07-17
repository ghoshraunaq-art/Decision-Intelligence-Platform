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


def total_revenue(region="All",
                  country="All",
                  category="All",
                  product="All",
                  year="All"):

    query = """

        SELECT
            COALESCE(SUM(s.quantity_sold * s.selling_price), 0)

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers cu
            ON o.customer_id = cu.customer_id

        JOIN regions r
            ON cu.region_id = r.region_id

        JOIN countries c
            ON r.country_id = c.country_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    if year != "All":
        query += " AND EXTRACT(YEAR FROM o.order_date) = %s"
        params.append(year)

    return execute_query(query, tuple(params))[0][0]

def total_products_sold(region="All",
                        country="All",
                        category="All",
                        product="All",
                        year="All"):

    query = """
        SELECT
            COALESCE(SUM(s.quantity_sold),0)

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers cu
            ON o.customer_id = cu.customer_id

        JOIN regions r
            ON cu.region_id = r.region_id

        JOIN countries c
            ON r.country_id = c.country_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    if year != "All":
        query += " AND EXTRACT(YEAR FROM o.order_date) = %s"
        params.append(year)

    return execute_query(query, tuple(params))[0][0]


def total_customers(region="All",
                    country="All",
                    category="All",
                    product="All",
                    year="All"):

    query = """
        SELECT
            COUNT(DISTINCT cu.customer_id)

        FROM customers cu

        JOIN regions r
            ON cu.region_id = r.region_id

        JOIN countries c
            ON r.country_id = c.country_id

        JOIN orders o
            ON cu.customer_id = o.customer_id

        JOIN order_items oi
            ON o.order_id = oi.order_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    if year != "All":
        query += " AND EXTRACT(YEAR FROM o.order_date) = %s"
        params.append(year)

    return execute_query(query, tuple(params))[0][0]


def total_orders(region="All",
                 country="All",
                 category="All",
                 product="All",
                 year="All"):

    query = """
        SELECT
            COUNT(DISTINCT o.order_id)

        FROM orders o

        JOIN customers cu
            ON o.customer_id = cu.customer_id

        JOIN regions r
            ON cu.region_id = r.region_id

        JOIN countries c
            ON r.country_id = c.country_id

        JOIN order_items oi
            ON o.order_id = oi.order_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    if year != "All":
        query += " AND EXTRACT(YEAR FROM o.order_date) = %s"
        params.append(year)

    return execute_query(query, tuple(params))[0][0]

def revenue_by_category(region="All",
                        country="All",
                        category="All",
                        product="All",
                        year="All"):

    query = """
        SELECT
            cat.category_name,
            SUM(s.quantity_sold * s.selling_price) AS revenue

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers cu
            ON o.customer_id = cu.customer_id

        JOIN regions r
            ON cu.region_id = r.region_id

        JOIN countries c
            ON r.country_id = c.country_id

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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    if year != "All":
        query += " AND EXTRACT(YEAR FROM o.order_date) = %s"
        params.append(year)

    query += """
        GROUP BY cat.category_name
        ORDER BY revenue DESC
    """

    return execute_query(query, tuple(params))

def revenue_by_region(region="All",
                      country="All",
                      category="All",
                      product="All",
                      year="All"):

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

        JOIN countries c
            ON r.country_id = c.country_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    if year != "All":
        query += " AND EXTRACT(YEAR FROM o.order_date) = %s"
        params.append(year)

    query += """
        GROUP BY r.region_name
        ORDER BY revenue DESC
    """

    return execute_query(query, tuple(params))


def top_products(region="All",
                 country="All",
                 category="All",
                 product="All",
                 year="All"):

    query = """
        SELECT
            p.product_name,
            SUM(s.quantity_sold) AS total_sold

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id = oi.order_item_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers cu
            ON o.customer_id = cu.customer_id

        JOIN regions r
            ON cu.region_id = r.region_id

        JOIN countries c
            ON r.country_id = c.country_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    if year != "All":
        query += " AND EXTRACT(YEAR FROM o.order_date) = %s"
        params.append(year)

    query += """
        GROUP BY p.product_name
        ORDER BY total_sold DESC
        LIMIT 10
    """

    return execute_query(query, tuple(params))

def top_customers(region="All",
                  country="All",
                  category="All",
                  product="All",
                  year="All"):

    query = """
        SELECT
            cu.customer_name,
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

        JOIN countries c
            ON r.country_id = c.country_id

        JOIN products p
            ON oi.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    if year != "All":
        query += " AND EXTRACT(YEAR FROM o.order_date) = %s"
        params.append(year)

    query += """
        GROUP BY cu.customer_name
        ORDER BY revenue DESC
        LIMIT 10
    """

    return execute_query(query, tuple(params))


def inventory_status(region="All",
                     country="All",
                     category="All",
                     product="All",
                     year="All"):

    query = """
        SELECT
            p.product_name,
            i.stock_quantity

        FROM inventory i

        JOIN products p
            ON i.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

        JOIN order_items oi
            ON p.product_id = oi.product_id

        JOIN orders o
            ON oi.order_id = o.order_id

        JOIN customers cu
            ON o.customer_id = cu.customer_id

        JOIN regions r
            ON cu.region_id = r.region_id

        JOIN countries c
            ON r.country_id = c.country_id

        WHERE 1=1
    """

    params=[]

    if region!="All":
        query+=" AND r.region_name=%s"
        params.append(region)

    if country!="All":
        query+=" AND c.country_name=%s"
        params.append(country)

    if category!="All":
        query+=" AND cat.category_name=%s"
        params.append(category)

    if product!="All":
        query+=" AND p.product_name=%s"
        params.append(product)

    if year!="All":
        query+=" AND EXTRACT(YEAR FROM o.order_date)=%s"
        params.append(year)

    query += """
        GROUP BY
            p.product_name,
            i.stock_quantity

        ORDER BY
            i.stock_quantity ASC

        LIMIT 10
    """

    return execute_query(query, tuple(params))

def monthly_revenue(region="All",
                    country="All",
                    category="All",
                    product="All",
                    year="All"):

    query="""
        SELECT
            TO_CHAR(o.order_date,'Mon YYYY'),
            SUM(s.quantity_sold*s.selling_price)

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id=oi.order_item_id

        JOIN orders o
            ON oi.order_id=o.order_id

        JOIN customers cu
            ON o.customer_id=cu.customer_id

        JOIN regions r
            ON cu.region_id=r.region_id

        JOIN countries c
            ON r.country_id=c.country_id

        JOIN products p
            ON oi.product_id=p.product_id

        JOIN categories cat
            ON p.category_id=cat.category_id

        WHERE 1=1
    """

    params=[]

    if region!="All":
        query+=" AND r.region_name=%s"
        params.append(region)

    if country!="All":
        query+=" AND c.country_name=%s"
        params.append(country)

    if category!="All":
        query+=" AND cat.category_name=%s"
        params.append(category)

    if product!="All":
        query+=" AND p.product_name=%s"
        params.append(product)

    if year!="All":
        query+=" AND EXTRACT(YEAR FROM o.order_date)=%s"
        params.append(year)

    query += """
        GROUP BY
            DATE_TRUNC('month',o.order_date),
            TO_CHAR(o.order_date,'Mon YYYY')

        ORDER BY
            DATE_TRUNC('month',o.order_date)
    """

    return execute_query(query, tuple(params))


def category_sales(region="All",
                   country="All",
                   category="All",
                   product="All",
                   year="All"):

    query="""
        SELECT
            cat.category_name,
            SUM(s.quantity_sold)

        FROM sales s

        JOIN order_items oi
            ON s.order_item_id=oi.order_item_id

        JOIN orders o
            ON oi.order_id=o.order_id

        JOIN customers cu
            ON o.customer_id=cu.customer_id

        JOIN regions r
            ON cu.region_id=r.region_id

        JOIN countries c
            ON r.country_id=c.country_id

        JOIN products p
            ON oi.product_id=p.product_id

        JOIN categories cat
            ON p.category_id=cat.category_id

        WHERE 1=1
    """

    params=[]

    if region!="All":
        query+=" AND r.region_name=%s"
        params.append(region)

    if country!="All":
        query+=" AND c.country_name=%s"
        params.append(country)

    if category!="All":
        query+=" AND cat.category_name=%s"
        params.append(category)

    if product!="All":
        query+=" AND p.product_name=%s"
        params.append(product)

    if year!="All":
        query+=" AND EXTRACT(YEAR FROM o.order_date)=%s"
        params.append(year)

    query += """
        GROUP BY
            cat.category_name

        ORDER BY
            2 DESC
    """

    return execute_query(query, tuple(params))

def available_regions(country="All"):

    query = """
        SELECT DISTINCT
            r.region_name
        FROM regions r
        JOIN countries c
            ON r.country_id = c.country_id
    """

    params = []

    if country != "All":
        query += """
        WHERE c.country_name = %s
        """
        params.append(country)

    query += """
        ORDER BY r.region_name
    """

    return execute_query(query, tuple(params))

def available_countries(region="All"):

    if region == "All":
        return execute_query("""
            SELECT DISTINCT
                country_name
            FROM countries
            ORDER BY country_name
        """)

    return execute_query("""
        SELECT DISTINCT
            c.country_name
        FROM regions r
        JOIN countries c
            ON r.country_id = c.country_id
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
        JOIN regions r
            ON cu.region_id = r.region_id
        JOIN countries c
            ON r.country_id = c.country_id
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
        JOIN regions r
            ON cu.region_id = r.region_id
        JOIN countries c
            ON r.country_id = c.country_id
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


def available_years(region="All",
                    country="All",
                    category="All",
                    product="All"):

    query = """
        SELECT DISTINCT
            EXTRACT(YEAR FROM o.order_date)
        FROM orders o
        JOIN customers cu
            ON o.customer_id = cu.customer_id
        JOIN regions r
            ON cu.region_id = r.region_id
        JOIN countries c
            ON r.country_id = c.country_id
        JOIN order_items oi
            ON o.order_id = oi.order_id
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN categories cat
            ON p.category_id = cat.category_id
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

    if product != "All":
        query += " AND p.product_name = %s"
        params.append(product)

    query += """
        ORDER BY
            EXTRACT(YEAR FROM o.order_date)
    """

    return execute_query(query, tuple(params))
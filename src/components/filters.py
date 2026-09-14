import streamlit as st

from analytics.sales_queries import (
    available_regions as get_available_regions,
    available_countries as get_available_countries,
    available_categories as get_available_categories,
    available_products as get_available_products,
    available_years as get_available_years,
)


# =========================================================
# Helper functions
# =========================================================

def flatten_rows(rows):
    """
    Convert SQL results such as:

        [('India',), ('Germany',)]

    into:

        ['India', 'Germany']
    """

    if rows is None:
        return []

    values = []

    for row in rows:
        if isinstance(row, (tuple, list)):
            if row:
                values.append(row[0])
        else:
            values.append(row)

    return values


def clean_options(values):
    """
    Remove None, blank values and duplicates.
    Always keep 'All' as the first option.
    """

    cleaned = []

    for value in values or []:
        if value is None:
            continue

        value = str(value).strip()

        if not value:
            continue

        if value != "All" and value not in cleaned:
            cleaned.append(value)

    return ["All"] + cleaned


def normalize_value(value):
    """
    Convert None or blank values into 'All'.
    """

    if value is None:
        return "All"

    value = str(value).strip()

    return value if value else "All"


# =========================================================
# Cached availability functions
# =========================================================
#
# These wrappers prevent the same filter query from being
# executed repeatedly during Streamlit reruns.
# =========================================================

@st.cache_data(ttl=600, show_spinner=False)
def cached_regions(country):
    return clean_options(
        flatten_rows(
            get_available_regions(country=country)
        )
    )


@st.cache_data(ttl=600, show_spinner=False)
def cached_countries(region):
    return clean_options(
        flatten_rows(
            get_available_countries(region=region)
        )
    )


@st.cache_data(ttl=600, show_spinner=False)
def cached_categories(region, country):
    return clean_options(
        flatten_rows(
            get_available_categories(
                region=region,
                country=country,
            )
        )
    )


@st.cache_data(ttl=600, show_spinner=False)
def cached_products(region, country, category):
    return clean_options(
        flatten_rows(
            get_available_products(
                region=region,
                country=country,
                category=category,
            )
        )
    )


@st.cache_data(ttl=600, show_spinner=False)
def cached_years(region, country, category, product):
    return clean_options(
        flatten_rows(
            get_available_years(
                region=region,
                country=country,
                category=category,
                product=product,
            )
        )
    )


# =========================================================
# Main filter component
# =========================================================

def create_filter_sidebar(
    prefix=None,
    available_regions=None,
    available_countries=None,
    available_categories=None,
    available_products=None,
    available_years=None,
):
    """
    Create the dashboard filter sidebar.

    All five filters remain enabled.

    Returns:

        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    """

    if prefix is None:
        prefix = "filters"

    # -----------------------------------------------------
    # Session-state keys
    # -----------------------------------------------------

    country_key = f"{prefix}_country"
    region_key = f"{prefix}_region"
    category_key = f"{prefix}_category"
    product_key = f"{prefix}_product"
    year_key = f"{prefix}_year"

    # -----------------------------------------------------
    # Initialize state
    # -----------------------------------------------------

    if country_key not in st.session_state:
        st.session_state[country_key] = "All"

    if region_key not in st.session_state:
        st.session_state[region_key] = "All"

    if category_key not in st.session_state:
        st.session_state[category_key] = "All"

    if product_key not in st.session_state:
        st.session_state[product_key] = "All"

    if year_key not in st.session_state:
        st.session_state[year_key] = "All"

    # -----------------------------------------------------
    # Read current selections
    # -----------------------------------------------------

    selected_country = normalize_value(
        st.session_state[country_key]
    )

    selected_region = normalize_value(
        st.session_state[region_key]
    )

    selected_category = normalize_value(
        st.session_state[category_key]
    )

    selected_product = normalize_value(
        st.session_state[product_key]
    )

    selected_year = normalize_value(
        st.session_state[year_key]
    )

    # -----------------------------------------------------
    # Load options
    # -----------------------------------------------------
    #
    # Important:
    # No five-pass repair loop.
    # No fallback query calls.
    # No disabled dropdowns.
    #
    # Every result is cached for 10 minutes.
    # -----------------------------------------------------

    try:
        region_options = cached_regions(
            selected_country
        )
    except Exception:
        region_options = ["All"]

    try:
        country_options = cached_countries(
            selected_region
        )
    except Exception:
        country_options = ["All"]

    try:
        category_options = cached_categories(
            selected_region,
            selected_country,
        )
    except Exception:
        category_options = ["All"]

    try:
        product_options = cached_products(
            selected_region,
            selected_country,
            selected_category,
        )
    except Exception:
        product_options = ["All"]

    try:
        year_options = cached_years(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
        )
    except Exception:
        year_options = ["All"]

    # -----------------------------------------------------
    # Keep current values valid
    # -----------------------------------------------------

    if selected_region not in region_options:
        selected_region = "All"

    if selected_country not in country_options:
        selected_country = "All"

    if selected_category not in category_options:
        selected_category = "All"

    if selected_product not in product_options:
        selected_product = "All"

    if selected_year not in year_options:
        selected_year = "All"

    # Save corrected values
    st.session_state[region_key] = selected_region
    st.session_state[country_key] = selected_country
    st.session_state[category_key] = selected_category
    st.session_state[product_key] = selected_product
    st.session_state[year_key] = selected_year

    # -----------------------------------------------------
    # Sidebar UI
    # -----------------------------------------------------

    st.sidebar.markdown("## 🎯 Filters")

    selected_country = st.sidebar.selectbox(
        "Country",
        country_options,
        key=country_key,
    )

    selected_region = st.sidebar.selectbox(
        "Region",
        region_options,
        key=region_key,
    )

    selected_category = st.sidebar.selectbox(
        "Category",
        category_options,
        key=category_key,
    )

    selected_product = st.sidebar.selectbox(
        "Product",
        product_options,
        key=product_key,
    )

    selected_year = st.sidebar.selectbox(
        "Year",
        year_options,
        key=year_key,
    )

    # -----------------------------------------------------
    # Apply button
    # -----------------------------------------------------

    if st.sidebar.button(
        "✅ Apply Filters",
        key=f"{prefix}_apply_filters",
    ):
        st.session_state[
            f"{prefix}_applied_country"
        ] = selected_country

        st.session_state[
            f"{prefix}_applied_region"
        ] = selected_region

        st.session_state[
            f"{prefix}_applied_category"
        ] = selected_category

        st.session_state[
            f"{prefix}_applied_product"
        ] = selected_product

        st.session_state[
            f"{prefix}_applied_year"
        ] = selected_year

    # -----------------------------------------------------
    # Return values
    # -----------------------------------------------------

    return (
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year,
    )
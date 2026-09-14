import streamlit as st

from src.analytics.sales_queries import (
    available_regions as get_available_regions,
    available_countries as get_available_countries,
    available_categories as get_available_categories,
    available_products as get_available_products,
    available_years as get_available_years,
)


def flatten_rows(rows):
    """
    Convert SQL results such as:

        [("India",), ("Germany",)]

    into:

        ["India", "Germany"]

    It also supports normal string lists.
    """
    values = []

    if rows is None:
        return values

    for row in rows:
        if isinstance(row, (tuple, list)):
            if len(row) > 0:
                values.append(row[0])
        else:
            values.append(row)

    return values


def clean_options(values):
    """
    Remove empty values and duplicates.
    Always keep 'All' as the first option.
    """
    cleaned = []

    for value in values or []:
        if value is None:
            continue

        value = str(value).strip()

        if value == "":
            continue

        if value != "All" and value not in cleaned:
            cleaned.append(value)

    return ["All"] + cleaned


def normalize_value(value):
    """
    Convert None or empty values into 'All'.
    """
    if value is None or str(value).strip() == "":
        return "All"

    return value


def create_filter_sidebar(
    prefix=None,
    available_regions=None,
    available_countries=None,
    available_categories=None,
    available_products=None,
    available_years=None,
):
    """
    Create interconnected dashboard filters.

    All filters remain enabled at all times.

    Returns:

        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    """

    if prefix is None:
        prefix = "filters"

    # ---------------------------------------------------------
    # Session-state keys
    # ---------------------------------------------------------

    country_key = f"{prefix}_country"
    region_key = f"{prefix}_region"
    category_key = f"{prefix}_category"
    product_key = f"{prefix}_product"
    year_key = f"{prefix}_year"

    previous_values_key = f"{prefix}_previous_filter_values"

    # ---------------------------------------------------------
    # Initial fallback options
    # ---------------------------------------------------------

    fallback_regions = clean_options(flatten_rows(available_regions))
    fallback_countries = clean_options(flatten_rows(available_countries))
    fallback_categories = clean_options(flatten_rows(available_categories))
    fallback_products = clean_options(flatten_rows(available_products))
    fallback_years = clean_options(flatten_rows(available_years))

    # ---------------------------------------------------------
    # Initialize session state
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Current filter values
    # ---------------------------------------------------------

    current_filters = {
        "country": normalize_value(st.session_state[country_key]),
        "region": normalize_value(st.session_state[region_key]),
        "category": normalize_value(st.session_state[category_key]),
        "product": normalize_value(st.session_state[product_key]),
        "year": normalize_value(st.session_state[year_key]),
    }

    # ---------------------------------------------------------
    # Get dynamic options
    # ---------------------------------------------------------

    def get_all_options(filters):
        """
        Every filter is calculated using the other four filters.
        """

        try:
            regions = clean_options(
                flatten_rows(
                    get_available_regions(
                        country=filters["country"],
                        category=filters["category"],
                        product=filters["product"],
                        year=filters["year"],
                    )
                )
            )
        except Exception:
            regions = fallback_regions

        try:
            countries = clean_options(
                flatten_rows(
                    get_available_countries(
                        region=filters["region"],
                        category=filters["category"],
                        product=filters["product"],
                        year=filters["year"],
                    )
                )
            )
        except Exception:
            countries = fallback_countries

        try:
            categories = clean_options(
                flatten_rows(
                    get_available_categories(
                        country=filters["country"],
                        region=filters["region"],
                        product=filters["product"],
                        year=filters["year"],
                    )
                )
            )
        except Exception:
            categories = fallback_categories

        try:
            products = clean_options(
                flatten_rows(
                    get_available_products(
                        country=filters["country"],
                        region=filters["region"],
                        category=filters["category"],
                        year=filters["year"],
                    )
                )
            )
        except Exception:
            products = fallback_products

        try:
            years = clean_options(
                flatten_rows(
                    get_available_years(
                        country=filters["country"],
                        region=filters["region"],
                        category=filters["category"],
                        product=filters["product"],
                    )
                )
            )
        except Exception:
            years = fallback_years

        return {
            "region": regions,
            "country": countries,
            "category": categories,
            "product": products,
            "year": years,
        }

    # ---------------------------------------------------------
    # Repair invalid selections
    # ---------------------------------------------------------

    # If a selected value is no longer available because of
    # another filter, reset only that value to 'All'.
    #
    # This loop prevents invalid combinations from remaining
    # inside Streamlit session state.

    for _ in range(5):
        options = get_all_options(current_filters)

        changed = False

        for filter_name in [
            "country",
            "region",
            "category",
            "product",
            "year",
        ]:
            selected_value = current_filters[filter_name]

            if selected_value not in options[filter_name]:
                current_filters[filter_name] = "All"
                changed = True

        if not changed:
            break

    # Save repaired values back into session state
    st.session_state[country_key] = current_filters["country"]
    st.session_state[region_key] = current_filters["region"]
    st.session_state[category_key] = current_filters["category"]
    st.session_state[product_key] = current_filters["product"]
    st.session_state[year_key] = current_filters["year"]

    # Recalculate final options after repairing selections
    options = get_all_options(current_filters)

    region_options = clean_options(options["region"])
    country_options = clean_options(options["country"])
    category_options = clean_options(options["category"])
    product_options = clean_options(options["product"])
    year_options = clean_options(options["year"])

    # ---------------------------------------------------------
    # Sidebar UI
    # ---------------------------------------------------------

    st.sidebar.markdown("## 🎯 Filters")

    # IMPORTANT:
    # No disabled=True is used anywhere.
    # All five filters remain active from the beginning.

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

    # ---------------------------------------------------------
    # Apply Filters button
    # ---------------------------------------------------------

    apply_button = st.sidebar.button(
        "✅ Apply Filters",
        key=f"{prefix}_apply_filters",
    )

    if apply_button:
        st.session_state[f"{prefix}_applied_country"] = selected_country
        st.session_state[f"{prefix}_applied_region"] = selected_region
        st.session_state[f"{prefix}_applied_category"] = selected_category
        st.session_state[f"{prefix}_applied_product"] = selected_product
        st.session_state[f"{prefix}_applied_year"] = selected_year

    # ---------------------------------------------------------
    # Store previous values
    # ---------------------------------------------------------

    st.session_state[previous_values_key] = {
        "country": selected_country,
        "region": selected_region,
        "category": selected_category,
        "product": selected_product,
        "year": selected_year,
    }

    # ---------------------------------------------------------
    # Return values in your existing expected order
    # ---------------------------------------------------------

    return (
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year,
    )
import streamlit as st


def create_filter_sidebar(
    prefix,
    available_regions,
    available_countries,
    available_categories,
    available_products,
    available_years,
):

    st.sidebar.markdown("---")
    st.sidebar.markdown("## 🎯 Filters")

    # ======================================================
    # DEFAULT FILTER VALUES
    # ======================================================

    defaults = {
        "country": "All",
        "region": "All",
        "category": "All",
        "product": "All",
        "year": "All",
    }

    for key, value in defaults.items():
        applied_key = f"{prefix}_{key}"

        if applied_key not in st.session_state:
            st.session_state[applied_key] = value

    # ======================================================
    # LIVE FILTER VALUES
    # ======================================================

    for key, value in defaults.items():
        live_key = f"{prefix}_{key}_live"

        if live_key not in st.session_state:
            st.session_state[live_key] = st.session_state[
                f"{prefix}_{key}"
            ]

    # ======================================================
    # COUNTRY
    # ======================================================

    country_live_key = f"{prefix}_country_live"

    country_options = ["All"] + [
        row[0]
        for row in available_countries()
    ]

    old_country = st.session_state[country_live_key]

    country = st.sidebar.selectbox(
        "Country",
        options=country_options,
        key=country_live_key,
    )

    # Reset all dependent filters when country changes
    if country != old_country:
        st.session_state[f"{prefix}_region_live"] = "All"
        st.session_state[f"{prefix}_category_live"] = "All"
        st.session_state[f"{prefix}_product_live"] = "All"
        st.session_state[f"{prefix}_year_live"] = "All"

    # ======================================================
    # REGION
    # ======================================================

    region_live_key = f"{prefix}_region_live"

    region_options = ["All"]

    if country != "All":
        region_options += [
            row[0]
            for row in available_regions(country)
        ]

    if st.session_state[region_live_key] not in region_options:
        st.session_state[region_live_key] = "All"

    region = st.sidebar.selectbox(
        "Region",
        options=region_options,
        key=region_live_key,
        disabled=(country == "All"),
    )

    # ======================================================
    # CATEGORY
    # ======================================================

    category_live_key = f"{prefix}_category_live"

    category_options = ["All"]

    # Category depends on Country, not Region.
    # Therefore, Category remains active when:
    # Country = Australia
    # Region = All

    if country != "All":
        category_options += [
            row[0]
            for row in available_categories(
                region=region,
                country=country,
            )
        ]

    if st.session_state[category_live_key] not in category_options:
        st.session_state[category_live_key] = "All"

    category = st.sidebar.selectbox(
        "Category",
        options=category_options,
        key=category_live_key,
        disabled=(country == "All"),
    )

    # ======================================================
    # PRODUCT
    # ======================================================

    product_live_key = f"{prefix}_product_live"

    product_options = ["All"]

    # Product depends on Category.
    # Region may remain All.

    if country != "All" and category != "All":
        product_options += [
            row[0]
            for row in available_products(
                region=region,
                country=country,
                category=category,
            )
        ]

    if st.session_state[product_live_key] not in product_options:
        st.session_state[product_live_key] = "All"

    product = st.sidebar.selectbox(
        "Product",
        options=product_options,
        key=product_live_key,
        disabled=(category == "All"),
    )

    # ======================================================
    # YEAR
    # ======================================================

    year_live_key = f"{prefix}_year_live"

    year_options = ["All"]

    if country != "All" and product != "All":
        year_options += [
            int(row[0])
            for row in available_years(
                region=region,
                country=country,
                category=category,
                product=product,
            )
        ]

    if st.session_state[year_live_key] not in year_options:
        st.session_state[year_live_key] = "All"

    year = st.sidebar.selectbox(
        "Year",
        options=year_options,
        key=year_live_key,
        disabled=(product == "All"),
    )

    # ======================================================
    # APPLY FILTERS
    # ======================================================

    if st.sidebar.button(
        "✅ Apply Filters",
        key=f"{prefix}_apply",
    ):
        st.session_state[f"{prefix}_country"] = country
        st.session_state[f"{prefix}_region"] = region
        st.session_state[f"{prefix}_category"] = category
        st.session_state[f"{prefix}_product"] = product
        st.session_state[f"{prefix}_year"] = year

    # ======================================================
    # RETURN APPLIED FILTERS
    # ======================================================

    return (
        st.session_state[f"{prefix}_region"],
        st.session_state[f"{prefix}_country"],
        st.session_state[f"{prefix}_category"],
        st.session_state[f"{prefix}_product"],
        st.session_state[f"{prefix}_year"],
    )
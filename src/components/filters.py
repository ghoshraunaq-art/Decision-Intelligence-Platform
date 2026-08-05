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

    # ------------------------
    # APPLIED FILTERS
    # ------------------------

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

    # ------------------------
    # LIVE FILTERS
    # ------------------------

    for key in defaults:

        live_key = f"{prefix}_{key}_live"

        if live_key not in st.session_state:
            st.session_state[live_key] = st.session_state[f"{prefix}_{key}"]

    # ======================================================
    # COUNTRY
    # ======================================================

    country_options = ["All"] + [
        r[0]
        for r in available_countries()
    ]

    old_country = st.session_state[f"{prefix}_country_live"]

    country = st.sidebar.selectbox(
        "Country",
        country_options,
        key=f"{prefix}_country_live"
    )

    if country != old_country:

        st.session_state[f"{prefix}_region_live"] = "All"
        st.session_state[f"{prefix}_category_live"] = "All"
        st.session_state[f"{prefix}_product_live"] = "All"
        st.session_state[f"{prefix}_year_live"] = "All"

    # ======================================================
    # REGION
    # ======================================================

    region_options = ["All"]

    if country != "All":
        region_options += [
            r[0]
            for r in available_regions(country)
        ]

    region = st.sidebar.selectbox(
        "Region",
        region_options,
        key=f"{prefix}_region_live",
        disabled=(country == "All")
    )

    # ======================================================
    # CATEGORY
    # ======================================================

    category_options = ["All"]

    if region != "All":

        category_options += [
            r[0]
            for r in available_categories(
                region,
                country
            )
        ]

    category = st.sidebar.selectbox(
        "Category",
        category_options,
        key=f"{prefix}_category_live",
        disabled=(region == "All")
    )

    # ======================================================
    # PRODUCT
    # ======================================================

    product_options = ["All"]

    if category != "All":

        product_options += [
            r[0]
            for r in available_products(
                region,
                country,
                category
            )
        ]

    product = st.sidebar.selectbox(
        "Product",
        product_options,
        key=f"{prefix}_product_live",
        disabled=(category == "All")
    )

    # ======================================================
    # YEAR
    # ======================================================

    year_options = ["All"]

    if product != "All":

        year_options += [
            int(r[0])
            for r in available_years(
                region,
                country,
                category,
                product
            )
        ]

    year = st.sidebar.selectbox(
        "Year",
        year_options,
        key=f"{prefix}_year_live",
        disabled=(product == "All")
    )

    # ======================================================
    # APPLY BUTTON
    # ======================================================

    if st.sidebar.button(
        "✅ Apply Filters",
        key=f"{prefix}_apply"
    ):

        st.session_state[f"{prefix}_country"] = country
        st.session_state[f"{prefix}_region"] = region
        st.session_state[f"{prefix}_category"] = category
        st.session_state[f"{prefix}_product"] = product
        st.session_state[f"{prefix}_year"] = year

    # ======================================================

    return (
        st.session_state[f"{prefix}_region"],
        st.session_state[f"{prefix}_country"],
        st.session_state[f"{prefix}_category"],
        st.session_state[f"{prefix}_product"],
        st.session_state[f"{prefix}_year"],
    )
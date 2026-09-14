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
    # DEFAULT VALUES
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
    # LIVE VALUES
    # ======================================================

    for key, value in defaults.items():
        live_key = f"{prefix}_{key}_live"

        if live_key not in st.session_state:
            st.session_state[live_key] = st.session_state[
                f"{prefix}_{key}"
            ]

    # ======================================================
    # RESET DEPENDENT FILTERS
    # ======================================================

    def reset_dependent_filters():
        st.session_state[f"{prefix}_region_live"] = "All"
        st.session_state[f"{prefix}_category_live"] = "All"
        st.session_state[f"{prefix}_product_live"] = "All"
        st.session_state[f"{prefix}_year_live"] = "All"

    # ======================================================
    # COUNTRY
    # ======================================================

    country_live_key = f"{prefix}_country_live"

    country_options = ["All"] + [
        row[0]
        for row in available_countries()
    ]

    country = st.sidebar.selectbox(
        "Country",
        options=country_options,
        key=country_live_key,
        on_change=reset_dependent_filters,
    )

    # ======================================================
    # REGION
    # ======================================================

    region_live_key = f"{prefix}_region_live"

    # When Country = All:
    #     Show all regions.
    #
    # When a specific Country is selected:
    #     Show only regions belonging to that country.

    if country == "All":
        region_options = ["All"] + [
            row[0]
            for row in available_regions()
        ]
    else:
        region_options = ["All"] + [
            row[0]
            for row in available_regions(
                country=country
            )
        ]

    # Prevent invalid/stale region selections.
    if st.session_state[region_live_key] not in region_options:
        st.session_state[region_live_key] = "All"

    region = st.sidebar.selectbox(
        "Region",
        options=region_options,
        key=region_live_key,
    )

    # ======================================================
    # CATEGORY
    # ======================================================

    category_live_key = f"{prefix}_category_live"

    # Category becomes available when either:
    # Country OR Region is selected.

    geography_selected = (
        country != "All"
        or region != "All"
    )

    category_options = ["All"]

    if geography_selected:
        category_options += [
            row[0]
            for row in available_categories(
                region=region,
                country=country,
            )
        ]

    # Prevent invalid/stale category selections.
    if st.session_state[category_live_key] not in category_options:
        st.session_state[category_live_key] = "All"

    category = st.sidebar.selectbox(
        "Category",
        options=category_options,
        key=category_live_key,
        disabled=not geography_selected,
    )

    # ======================================================
    # PRODUCT
    # ======================================================

    product_live_key = f"{prefix}_product_live"

    product_options = ["All"]

    # Product becomes available only after Category
    # has been selected.

    if category != "All":
        product_options += [
            row[0]
            for row in available_products(
                region=region,
                country=country,
                category=category,
            )
        ]

    # Prevent invalid/stale product selections.
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

    # Year becomes available only after Product
    # has been selected.

    if product != "All":
        year_options += [
            int(row[0])
            for row in available_years(
                region=region,
                country=country,
                category=category,
                product=product,
            )
        ]

    # Prevent invalid/stale year selections.
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
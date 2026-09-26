import streamlit as st

from analytics.sales_queries import (
    available_filter_options,
)


# ============================================================
# HELPERS
# ============================================================

def normalize_value(value):
    """Normalize empty values to All."""

    if value is None:
        return "All"

    value = str(value).strip()

    if not value:
        return "All"

    return value


# ============================================================
# HIDE STREAMLIT RUN STATUS
# ============================================================

st.markdown(
    """
    <style>
        div[data-testid="stStatusWidget"] {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FILTER SIDEBAR
# ============================================================

@st.fragment
def create_filter_sidebar(
    prefix=None,
    available_regions=None,
    available_countries=None,
    available_categories=None,
    available_products=None,
    available_years=None,
):
    """
    Hierarchical filter system:

        Country
            ↓
        Region
            ↓
        Category
            ↓
        Product
            ↓
        Year
            ↓
        Apply Filters

    'All' is a valid selection at every level.

    Dashboard data changes ONLY after Apply Filters.
    """

    if prefix is None:
        prefix = "filters"


    # ========================================================
    # SESSION STATE KEYS
    # ========================================================

    country_key = f"{prefix}_country"
    region_key = f"{prefix}_region"
    category_key = f"{prefix}_category"
    product_key = f"{prefix}_product"
    year_key = f"{prefix}_year"

    applied_country_key = f"{prefix}_applied_country"
    applied_region_key = f"{prefix}_applied_region"
    applied_category_key = f"{prefix}_applied_category"
    applied_product_key = f"{prefix}_applied_product"
    applied_year_key = f"{prefix}_applied_year"


    # ========================================================
    # INITIAL LIVE VALUES
    # ========================================================

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


    # ========================================================
    # INITIAL APPLIED VALUES
    # ========================================================

    if applied_country_key not in st.session_state:
        st.session_state[applied_country_key] = "All"

    if applied_region_key not in st.session_state:
        st.session_state[applied_region_key] = "All"

    if applied_category_key not in st.session_state:
        st.session_state[applied_category_key] = "All"

    if applied_product_key not in st.session_state:
        st.session_state[applied_product_key] = "All"

    if applied_year_key not in st.session_state:
        st.session_state[applied_year_key] = "All"


    # ========================================================
    # CURRENT SELECTIONS
    # ========================================================

    country = normalize_value(
        st.session_state[country_key]
    )

    region = normalize_value(
        st.session_state[region_key]
    )

    category = normalize_value(
        st.session_state[category_key]
    )

    product = normalize_value(
        st.session_state[product_key]
    )

    year = normalize_value(
        st.session_state[year_key]
    )


    # ========================================================
    # ONE DATABASE REQUEST
    # ========================================================

    options = available_filter_options(
        country=country,
        region=region,
        category=category,
        product=product,
    )

    country_options = options["country"]
    region_options = options["region"]
    category_options = options["category"]
    product_options = options["product"]
    year_options = options["year"]


    # ========================================================
    # VALIDATE CURRENT VALUES
    # ========================================================

    if country not in country_options:

        country = "All"

        st.session_state[country_key] = "All"


    if region not in region_options:

        region = "All"

        st.session_state[region_key] = "All"


    if category not in category_options:

        category = "All"

        st.session_state[category_key] = "All"


    if product not in product_options:

        product = "All"

        st.session_state[product_key] = "All"


    if year not in year_options:

        year = "All"

        st.session_state[year_key] = "All"


    # ========================================================
    # HIERARCHY
    #
    # All counts as a valid selection.
    # ========================================================

    country_selected = (
        country in country_options
    )

    region_selected = (
        region in region_options
    )

    category_selected = (
        category in category_options
    )

    product_selected = (
        product in product_options
    )


    # ========================================================
    # SIDEBAR
    # ========================================================

    st.markdown(
        "## 🎯 Filters"
    )


    # ========================================================
    # COUNTRY
    # ========================================================

    st.selectbox(
        "Country",
        country_options,
        key=country_key,
    )


    # ========================================================
    # REGION
    # ========================================================

    st.selectbox(
        "Region",
        region_options,
        key=region_key,
        disabled=not country_selected,
    )


    # ========================================================
    # CATEGORY
    # ========================================================

    st.selectbox(
        "Category",
        category_options,
        key=category_key,
        disabled=not (
            country_selected
            and region_selected
        ),
    )


    # ========================================================
    # PRODUCT
    # ========================================================

    st.selectbox(
        "Product",
        product_options,
        key=product_key,
        disabled=not (
            country_selected
            and region_selected
            and category_selected
        ),
    )


    # ========================================================
    # YEAR
    # ========================================================

    st.selectbox(
        "Year",
        year_options,
        key=year_key,
        disabled=not (
            country_selected
            and region_selected
            and category_selected
            and product_selected
        ),
    )


    # ========================================================
    # APPLY FILTERS
    # ========================================================

    year_enabled = (
        country_selected
        and region_selected
        and category_selected
        and product_selected
    )


    apply_clicked = st.button(
        "✅ Apply Filters",
        key=f"{prefix}_apply_filters",
        type="primary",
        use_container_width=True,
        disabled=not year_enabled,
    )


    # ========================================================
    # APPLY
    # ========================================================

    if apply_clicked:

        st.session_state[applied_country_key] = normalize_value(
            st.session_state[country_key]
        )

        st.session_state[applied_region_key] = normalize_value(
            st.session_state[region_key]
        )

        st.session_state[applied_category_key] = normalize_value(
            st.session_state[category_key]
        )

        st.session_state[applied_product_key] = normalize_value(
            st.session_state[product_key]
        )

        st.session_state[applied_year_key] = normalize_value(
            st.session_state[year_key]
        )

        st.rerun()


    # ========================================================
    # RETURN ONLY APPLIED FILTERS
    # ========================================================

    return (
        st.session_state[applied_region_key],
        st.session_state[applied_country_key],
        st.session_state[applied_category_key],
        st.session_state[applied_product_key],
        st.session_state[applied_year_key],
    )
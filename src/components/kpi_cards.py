import streamlit as st


def format_currency(value):

    if value >= 10000000:
        return f"₹ {value/10000000:.2f} Cr"

    elif value >= 100000:
        return f"₹ {value/100000:.2f} Lakh"

    else:
        return f"₹ {value:,.2f}"


def show_kpi_cards(
    revenue,
    products,
    customers,
    orders,
    top_category,
    top_category_revenue
):

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💰 Total Revenue",
            format_currency(revenue)
        )

    with col2:
        st.metric(
            "📦 Products Sold",
            f"{products:,}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric(
            "👥 Registered Customers",
            f"{customers:,}"
        )

    with col4:
        st.metric(
            "📑 Total Orders",
            f"{orders:,}"
        )

    with col5:
        st.metric(
            "🏆 Top Revenue Category",
            top_category,
            format_currency(top_category_revenue)
        )
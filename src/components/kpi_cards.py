import streamlit as st


def show_kpi_cards(
    revenue,
    products,
    customers,
    orders
):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💰 Total Revenue",
            f"₹ {revenue:,.2f}"
        )

    with col2:
        st.metric(
            "📦 Products Sold",
            f"{products:,}"
        )

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
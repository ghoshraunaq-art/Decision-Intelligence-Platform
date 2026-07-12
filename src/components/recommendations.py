import streamlit as st


def show_recommendations(inventory):

    st.header("🤖 AI Business Recommendations")

    low_stock = []

    for product, stock in inventory:

        if stock < 50:
            low_stock.append(product)

    if low_stock:

        st.warning(
            "Low Stock Products:\n\n• "
            + "\n• ".join(low_stock)
        )

    else:

        st.success(
            "Inventory levels look healthy."
        )
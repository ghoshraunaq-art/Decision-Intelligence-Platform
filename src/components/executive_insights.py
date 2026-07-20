import streamlit as st


def show_executive_insights(
        revenue,
        products,
        inventory,
        customers
):

    st.subheader("🤖 Executive AI Insights")


    insights = []


    if revenue > 0:
        insights.append(
            f"💰 Total revenue generated: ${revenue:,.2f}"
        )


    if len(products) > 0:

        top_product = products.iloc[0]["Product"]

        insights.append(
            f"🏆 Best performing product: {top_product}"
        )


    if len(inventory) > 0:

        low_stock = inventory[
            inventory["Stock"] < 50
        ]

        if len(low_stock) > 0:

            insights.append(
                f"⚠️ {len(low_stock)} products require inventory attention"
            )


    if len(customers) > 0:

        top_customer = customers.iloc[0]["Customer"]

        insights.append(
            f"👑 Highest value customer: {top_customer}"
        )


    for insight in insights:

        st.info(insight)
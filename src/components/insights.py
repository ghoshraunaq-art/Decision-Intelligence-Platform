import streamlit as st


def show_insights(
    revenue_data,
    category_data,
    region_data,
    inventory_data,
    revenue_category_data
):

    st.subheader("📊 Automated Business Insights")

    insights = []

    if revenue_data:
        best_month = max(
            revenue_data,
            key=lambda x: x[1]
        )

        insights.append(
            f"📈 Highest revenue month: {best_month[0]} with revenue of {best_month[1]:,.2f}"
        )


    if category_data:
        best_category = max(
            category_data,
            key=lambda x: x[1]
        )

        insights.append(
            f"📦 Top category by sales volume: {best_category[0]}"
        )


    if revenue_category_data:
        insights.append(
            f"💰 Top category by revenue: {revenue_category_data[0]}"
        )


    if region_data:
        best_region = max(
            region_data,
            key=lambda x: x[1]
        )

        insights.append(
            f"🌍 Highest revenue region: {best_region[0]}"
        )


    if inventory_data:

        low_stock = [
            item[0]
            for item in inventory_data
            if item[1] < 50
        ]

        if low_stock:
            insights.append(
                f"⚠ Low inventory alert: {', '.join(low_stock)}"
            )


    for insight in insights:
        st.info(insight)
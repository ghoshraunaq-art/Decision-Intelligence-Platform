import streamlit as st


def show_business_health(
    revenue,
    orders,
    customers,
    inventory_df
):

    if customers == 0:
        aov = 0
    else:
        aov = revenue / orders


    low_stock_count = len(
        inventory_df[
            inventory_df["Stock"] < 50
        ]
    )


    score = 100


    if low_stock_count > 3:
        score -= 20

    elif low_stock_count > 0:
        score -= 10


    if aov < 50000:
        score -= 10


    st.subheader("📊 Business Health Score")


    if score >= 80:
        st.success(
            f"🟢 Excellent Business Health: {score}/100"
        )

    elif score >= 60:
        st.warning(
            f"🟡 Moderate Business Health: {score}/100"
        )

    else:
        st.error(
            f"🔴 Poor Business Health: {score}/100"
        )


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "Average Order Value",
            f"₹ {aov:,.2f}"
        )


    with col2:
        st.metric(
            "Inventory Risk Items",
            low_stock_count
        )


    with col3:
        st.metric(
            "Customer Base",
            customers
        )
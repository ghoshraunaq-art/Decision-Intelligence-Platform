import streamlit as st
import pandas as pd
import plotly.express as px


def show_customer_intelligence(customers_data):

    if not customers_data:
        return


    df = pd.DataFrame(
        customers_data,
        columns=[
            "Customer",
            "Revenue"
        ]
    )


    avg_revenue = df["Revenue"].mean()

    top_customer = df.loc[
        df["Revenue"].idxmax()
    ]


    st.subheader("👥 Customer Intelligence")


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Average Customer Value",
            f"₹ {avg_revenue:,.2f}"
        )


    with col2:

        st.metric(
            "Highest Value Customer",
            top_customer["Customer"]
        )


    fig = px.bar(
        df,
        x="Customer",
        y="Revenue",
        title="Customer Revenue Distribution"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )
import streamlit as st
import pandas as pd
import plotly.express as px


def show_customer_churn(data):

    st.subheader("🚪 Customer Churn Prediction")

    if len(data) == 0:
        st.warning("No customer data available.")
        return

    df = pd.DataFrame(
        data,
        columns=[
            "Customer",
            "Last Purchase",
            "Frequency",
            "Revenue",
            "Days Since Purchase",
            "Churn Risk"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    churn_counts = (
        df["Churn Risk"]
        .value_counts()
        .reset_index()
    )

    churn_counts.columns = [
        "Risk",
        "Customers"
    ]

    fig = px.bar(
        churn_counts,
        x="Risk",
        y="Customers",
        color="Risk",
        title="Customer Churn Risk Distribution",
        text="Customers",
        color_discrete_map={
            "🟢 Low": "#2ecc71",
            "🟡 Medium": "#f1c40f",
            "🔴 High": "#e74c3c"
        }
    )

    fig.update_layout(
        height=450,
        xaxis_title="",
        yaxis_title="Number of Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
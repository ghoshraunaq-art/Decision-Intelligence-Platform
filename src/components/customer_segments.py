import streamlit as st
import pandas as pd
import plotly.express as px


def show_customer_segments(data):

    st.subheader("👥 Customer Segmentation")

    if len(data) == 0:
        st.warning("No customer data.")
        return

    df = pd.DataFrame(
        data,
        columns=[
            "Customer",
            "Last Purchase",
            "Frequency",
            "Revenue"
        ]
    )

    df["Revenue"] = df["Revenue"].astype(float)
    df["Frequency"] = df["Frequency"].astype(int)

    revenue75 = df["Revenue"].quantile(0.75)
    revenue40 = df["Revenue"].quantile(0.40)

    def segment(x):

        if x >= revenue75:
            return "VIP"

        elif x >= revenue40:
            return "Regular"

        return "Low Value"

    df["Segment"] = df["Revenue"].apply(segment)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )   

    segment_order = ["Low Value", "Regular", "VIP"]

    segment_count = (
        df["Segment"]
        .value_counts()
        .reindex(segment_order, fill_value=0)
        .reset_index()
    )

    segment_count.columns = [
        "Segment",
        "Customers"
    ]

    fig = px.bar(
        segment_count,
        x="Segment",
        y="Customers",
        color="Segment",
        category_orders={"Segment": segment_order},
        title="Customer Segmentation"
    )

    fig.update_xaxes(
        tickangle=-45,
        automargin=True
    )

    fig.update_layout(
        height=500,
        margin=dict(b=120),
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
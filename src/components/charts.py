import streamlit as st
import pandas as pd
import plotly.express as px


def show_revenue_category_chart(data):

    df = pd.DataFrame(
        data,
        columns=["Category", "Revenue"]
    )

    # Sort categories by revenue
    df = df.sort_values("Revenue", ascending=True)

    fig = px.bar(
        df,
        x="Revenue",
        y="Category",
        orientation="h",
        color="Revenue",
        title="Revenue Distribution by Product Category",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        height=500,
        showlegend=False,
        yaxis_title="Category",
        xaxis_title="Revenue",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="category_chart"
    )


def show_region_chart(data):

    df = pd.DataFrame(
        data,
        columns=["Region", "Revenue"]
    )

    fig = px.pie(
        df,
        names="Region",
        values="Revenue",
        title="Revenue Contribution by Region",
        hole=0.35
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent"
    )

    fig.update_layout(
        height=500,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="region_chart"
    )
import streamlit as st
import pandas as pd
import plotly.express as px


def show_revenue_category_chart(data):

    df = pd.DataFrame(
        data,
        columns=["Category", "Revenue"]
    )

    fig = px.bar(
        df,
        x="Category",
        y="Revenue",
        color="Revenue",
        title="Revenue Distribution by Product Category"
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
        title="Revenue Contribution by Region"
    )

    st.plotly_chart(
    fig,
    use_container_width=True,
    key="region_chart"
)
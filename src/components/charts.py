import streamlit as st
import pandas as pd
import plotly.express as px


def show_revenue_category_chart(data):

    df = pd.DataFrame(
        data,
        columns=["Category", "Revenue"]
    )

    df = df.sort_values(
        "Revenue",
        ascending=True
    )

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
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=40
        )
    )

    fig.update_xaxes(
        nticks=6,
        tickangle=0,
        tickformat=",.0f",
        automargin=True
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

    # Top 10 Highest Revenue Regions
    df = (
        df.sort_values(
            by="Revenue",
            ascending=False
        )
        .head(10)
        .reset_index(drop=True)
    )

    fig = px.bar(
        df,
        x="Revenue",
        y="Region",
        orientation="h",
        color="Region",
        color_discrete_sequence=px.colors.qualitative.Vivid,
        title="Top Revenue Generating Regions"
    )

    # Remove labels completely
    fig.update_traces(
        text=None,
        hovertemplate="<b>%{y}</b><br>Revenue: ₹ %{x:,.2f}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        showlegend=False,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        yaxis_title="Region",
        xaxis_title="Revenue"
    )

    # Highest revenue at TOP
    fig.update_yaxes(
        autorange="reversed"
    )

    # Cleaner x-axis
    fig.update_xaxes(
        tickformat=",.0f",
        nticks=6,
        automargin=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="region_chart"
    )
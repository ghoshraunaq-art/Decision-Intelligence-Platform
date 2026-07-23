import pandas as pd
import plotly.express as px


def show_forecast(data):

    if not data:
        return None

    df = pd.DataFrame(
        data,
        columns=["Month", "Revenue"]
    )

    df["Month"] = pd.to_datetime(df["Month"])

    df = df.sort_values("Month")

    fig = px.line(
        df,
        x="Month",
        y="Revenue",
        markers=True,
        title="📈 Revenue Trend Forecast"
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8)
    )

    fig.update_layout(
        height=500,
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis_title="Month",
        yaxis_title="Revenue",
        hovermode="x unified"
    )

    fig.update_xaxes(
        tickformat="%b %Y",
        tickangle=-45,
        automargin=True
    )

    return fig
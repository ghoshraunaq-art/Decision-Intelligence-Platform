import pandas as pd
import plotly.express as px


def show_forecast(data):

    if not data:
        return None

    df = pd.DataFrame(
        data,
        columns=["Month", "Revenue"]
    )

    df["Month"] = pd.to_datetime(
        df["Month"]
    )

    df = df.sort_values(
        "Month"
    )

    fig = px.line(
        df,
        x="Month",
        y="Revenue",
        markers=True,
        title="Revenue Trend Forecast"
    )

    return fig
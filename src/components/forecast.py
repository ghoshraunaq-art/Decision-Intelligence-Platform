import pandas as pd
import plotly.express as px


def show_forecast(data):

    st_title = "📈 Revenue Forecast"

    if data.empty:
        return

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
        title=st_title
    )

    return fig
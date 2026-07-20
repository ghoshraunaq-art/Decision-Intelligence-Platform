import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression


def show_forecast(monthly_data):

    st.subheader("🔮 Revenue Forecast")

    if len(monthly_data) < 3:
        st.warning(
            "Not enough data for forecasting"
        )
        return


    df = pd.DataFrame(
        monthly_data,
        columns=[
            "Month",
            "Revenue"
        ]
    )


    df["Month_Index"] = range(
        len(df)
    )


    model = LinearRegression()

    model.fit(
        df[["Month_Index"]],
        df["Revenue"]
    )


    future_months = pd.DataFrame(
        {
            "Month_Index":
            [
                len(df),
                len(df)+1,
                len(df)+2,
                len(df)+3,
                len(df)+4,
                len(df)+5
            ]
        }
    )


    predictions = model.predict(
        future_months
    )


    forecast_df = pd.DataFrame(
        {
            "Future Month":
            [
                "Month +1",
                "Month +2",
                "Month +3",
                "Month +4",
                "Month +5",
                "Month +6"
            ],
            "Predicted Revenue":
            predictions
        }
    )


    st.line_chart(
        forecast_df.set_index(
            "Future Month"
        )
    )


    st.dataframe(
        forecast_df,
        use_container_width=True
    )
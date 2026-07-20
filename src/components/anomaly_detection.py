import streamlit as st
import pandas as pd


def show_anomaly_detection(monthly_data):

    st.subheader("🚨 Revenue Anomaly Detection")

    if len(monthly_data) < 3:
        st.warning(
            "Not enough data for anomaly detection"
        )
        return


    df = pd.DataFrame(
        monthly_data,
        columns=[
            "Month",
            "Revenue"
        ]
    )


    df["Revenue"] = df["Revenue"].astype(float)


    mean_revenue = df["Revenue"].mean()

    std_revenue = df["Revenue"].std()


    upper_limit = mean_revenue + (2 * std_revenue)

    lower_limit = mean_revenue - (2 * std_revenue)


    def detect(value):

        if value > upper_limit:
            return "📈 Revenue Spike"

        elif value < lower_limit:
            return "📉 Revenue Drop"

        else:
            return "✅ Normal"


    df["Status"] = df["Revenue"].apply(
        detect
    )


    anomalies = df[
        df["Status"] != "✅ Normal"
    ]


    if len(anomalies) > 0:

        st.error(
            "Anomalies detected!"
        )

        st.dataframe(
            anomalies,
            width="stretch",
            hide_index=True
        )

    else:

        st.success(
            "No unusual revenue patterns detected."
        )


    st.line_chart(
        df.set_index("Month")["Revenue"]
    )
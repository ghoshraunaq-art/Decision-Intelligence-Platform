import streamlit as st
import pandas as pd
import plotly.express as px


def show_anomaly_detection(monthly_data):

    st.subheader("🚨 Revenue Anomaly Detection")

    if len(monthly_data) < 3:
        st.warning("Not enough data for anomaly detection")
        return

    df = pd.DataFrame(
        monthly_data,
        columns=["Month", "Revenue"]
    )

    df["Revenue"] = df["Revenue"].astype(float)

    # Convert month to datetime so Plotly sorts correctly
    df["Month"] = pd.to_datetime(df["Month"])
    df = df.sort_values("Month")

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

    df["Status"] = df["Revenue"].apply(detect)

    anomalies = df[df["Status"] != "✅ Normal"]

    if len(anomalies):
        st.error("Anomalies detected!")
        st.dataframe(
            anomalies,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.success("No unusual revenue patterns detected.")

    fig = px.line(
        df,
        x="Month",
        y="Revenue",
        markers=True,
        title="Revenue Trend"
    )

    fig.update_layout(
        height=500,
        xaxis_title="Month",
        yaxis_title="Revenue",
        xaxis=dict(
            tickformat="%b %Y",
            tickangle=-45,
            automargin=True
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
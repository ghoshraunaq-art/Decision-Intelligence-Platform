import streamlit as st
import pandas as pd


def show_customer_segments(data):

    st.subheader("👥 Customer Segmentation")

    if len(data)==0:
        st.warning("No customer data.")
        return

    df=pd.DataFrame(
        data,
        columns=[
            "Customer",
            "Last Purchase",
            "Frequency",
            "Revenue"
        ]
    )

    revenue75=df["Revenue"].quantile(.75)
    revenue40=df["Revenue"].quantile(.40)

    def segment(x):

        if x>=revenue75:
            return "VIP"

        elif x>=revenue40:
            return "Regular"

        return "Low Value"

    df["Segment"]=df["Revenue"].apply(segment)

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

    st.bar_chart(
        df["Segment"].value_counts()
    )
import streamlit as st
import pandas as pd


def upload_page():

    st.title("📂 Business Data Upload")

    st.write(
        "Upload your business transaction data and generate analytics automatically."
    )

    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )


    if uploaded_file:

        try:
            df = pd.read_csv(uploaded_file, encoding="utf-8")

        except UnicodeDecodeError:
            df = pd.read_csv(uploaded_file, encoding="latin1")

        st.success("File uploaded successfully!")

        st.subheader("Preview")

        st.dataframe(df.head())


if __name__ == "__main__":
    upload_page()
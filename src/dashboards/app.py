import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from components.kpi_cards import show_kpi_cards
from components.charts import (
    show_revenue_category_chart,
    show_region_chart
)
from components.recommendations import show_recommendations
from components.insights import show_insights
from components.forecast import show_forecast
from components.customer_segments import show_customer_segments
from components.business_health import show_business_health
from components.customer_intelligence import show_customer_intelligence
from components.anomaly_detection import show_anomaly_detection
from components.executive_insights import show_executive_insights
from components.customer_churn import show_customer_churn

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from analytics.sales_queries import (
    total_revenue,
    total_products_sold,
    total_customers,
    total_orders,
    revenue_by_category,
    revenue_by_region,
    available_regions,
    available_countries,
    available_categories,
    available_products,
    available_years,
    top_products,
    top_customers,
    inventory_status,
    monthly_revenue,
    category_sales,
    top_category_by_revenue,
    customer_segmentation,
    customer_churn_prediction,
    product_recommendations,
)

st.set_page_config(
    page_title="Decision Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
/* Keep the dropdown list above everything else */
div[data-baseweb="popover"] {
    z-index: 9999 !important;
}

/* Give the dropdown list itself a generous scrollable height */
ul[role="listbox"] {
    max-height: 320px !important;
    overflow-y: auto !important;
}

/* Add real scroll room below the sidebar's last filter so opening a
   dropdown near the bottom always has space to expand into, and you
   can scroll further down to reach every option manually */
section[data-testid="stSidebar"] > div:first-child {
    padding-bottom: 350px !important;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🧠 Decision Intelligence")

page = st.sidebar.radio(
    "📂 Navigation",
    [
        "🏠 Dashboard",
        "📈 Analytics",
        "💡 Recommendations"
    ]
)

# ===========================
# DASHBOARD
# ===========================

if page == "🏠 Dashboard":

    st.sidebar.markdown("---")
    st.sidebar.markdown("## 🎯 Filters")

    # Country
    country_options = ["All"] + [
    row[0] for row in available_countries()
    ]

    selected_country = st.sidebar.selectbox(
        "Country",
        country_options
    )

    # Region
    region_options = ["All"] + [
    row[0]
    for row in available_regions(selected_country)
    ]

    selected_region = st.sidebar.selectbox(
        "Region",
        region_options
    )

    # Category
    category_options = ["All"] + [
        row[0] for row in available_categories(
            selected_region,
            selected_country
        )
    ]

    selected_category = st.sidebar.selectbox(
        "Category",
        category_options
    )

    # Product
    product_options = ["All"] + [
        row[0] for row in available_products(
            selected_region,
            selected_country,
            selected_category
        )
    ]

    selected_product = st.sidebar.selectbox(
        "Product",
        product_options
    )

    # Year
    year_options = ["All"] + [
    int(row[0]) for row in available_years(
        selected_region,
        selected_country,
        selected_category,
        selected_product
    )
    ]

    selected_year = st.sidebar.selectbox(
        "Year",
        year_options
    )
    
    st.title("📊 Decision Intelligence Platform")

    st.subheader("Interactive Decision Intelligence Dashboard")

    st.markdown(
    """
    Monitor **Sales, Customers, Products, Inventory, Forecasts, and Business Performance**
    through an interactive analytics dashboard powered by:

    - 🐍 Python
    - 🐘 PostgreSQL
    - ⚡ Streamlit
    - 📊 Plotly
    """
    )

    st.divider()

    top_category_data = top_category_by_revenue(
    selected_region,
    selected_country,
    selected_category,
    selected_product,
    selected_year
)

    show_kpi_cards(
        total_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        total_products_sold(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        total_customers(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        total_orders(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        top_category_data[0],
        top_category_data[1]
    )

    st.divider()

    st.subheader("📌 Executive Summary")

    left, right = st.columns(2)

    with left:
        st.info("""
### Business Performance

• Revenue analysis across products and regions

• Inventory monitoring

• Customer purchase behaviour analysis

• Region-wise business performance
""")

    with right:
        st.success("""
### Strategic Recommendations

• Increase stock of high-performing products

• Improve low-performing categories

• Expand profitable regions

• Monitor inventory before stock-outs
""")

    st.divider()

    left, right = st.columns(2)

    with left:
        show_revenue_category_chart(
            revenue_by_category(
                selected_region,
                selected_country,
                selected_category,
                selected_product,
                selected_year
            )
        )

    with right:
        show_region_chart(
            revenue_by_region(
                selected_region,
                selected_country,
                selected_category,
                selected_product,
                selected_year
            )
        )

    st.divider()

    st.header("📊 Advanced Analytics")

    left, right = st.columns(2)

    products_df = pd.DataFrame(
       top_products(
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    ),
    columns=["Product", "Units Sold"]
    )

    fig_products = px.bar(
    products_df,
    x="Units Sold",
    y="Product",
    orientation="h",
    title="Top Selling Products"
)

    fig_products.update_layout(
        template="plotly_dark",
        height=500,
        yaxis=dict(
            tickfont=dict(size=13)
        )
    )

    fig_products.update_xaxes(
        nticks=6,
        tickformat=",.0f",
        tickfont=dict(size=12),
        automargin=True
    )

    with left:
        st.plotly_chart(
            fig_products,
            width="stretch"
        )

    customers_df = pd.DataFrame(
       top_customers(
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    ),
    columns=["Customer", "Revenue"]
    )

    fig_customers = px.bar(
    customers_df,
    x="Revenue",
    y="Customer",
    orientation="h",
    title="Top Customers"
)

    fig_customers.update_layout(
        template="plotly_dark",
        height=500,
        xaxis=dict(
            tickformat="~s",
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            tickfont=dict(size=13)
        )
    )

    with right:
        st.plotly_chart(
            fig_customers,
            width="stretch"
        )

    st.divider()

    st.header("📦 Inventory Status")

    inventory_df = pd.DataFrame(
        inventory_status(
    selected_region,
    selected_country,
    selected_category,
    selected_product,
    selected_year
        ),
    columns=["Product", "Stock"]
    )

    st.dataframe(
        inventory_df,
        width="stretch"
    )

    st.divider()

    left, right = st.columns(2)

    monthly_df = pd.DataFrame(
        monthly_revenue(
    selected_region,
    selected_country,
    selected_category,
    selected_product,
    selected_year
        ),
        columns=["Month", "Revenue"]
    )

    monthly_df["Month"] = pd.to_datetime(monthly_df["Month"])

    fig_month = px.line(
        monthly_df,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue"
    )

    fig_month.update_layout(
        template="plotly_dark",
        height=500
    )

    fig_month.update_xaxes(
        tickformat="%b %Y",
        dtick="M1",
        tickangle=-45,
        tickfont=dict(size=12)
    )

    with left:
        st.plotly_chart(
            fig_month,
            width="stretch"
        )

    category_sales_df = pd.DataFrame(
        category_sales(
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    ),
    columns=["Category", "Units Sold"]
    )

    fig_sales = px.pie(
        category_sales_df,
        names="Category",
        values="Units Sold",
        title="Sales Distribution"
    )

    with right:
        st.plotly_chart(
            fig_sales,
            width="stretch"
        )

    st.divider()

    show_insights(
        monthly_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        category_sales(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        revenue_by_region(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        inventory_status(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        top_category_by_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        )
    )

    st.divider()

    forecast_fig = show_forecast(
        monthly_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        )
    )

    if forecast_fig:
        st.subheader("📈 Revenue Trend Forecast")
        st.plotly_chart(
            forecast_fig,
            width="stretch"
        )

    st.divider()

    show_anomaly_detection(
        monthly_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        )
    )

    st.divider()

    show_customer_segments(
        customer_segmentation(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        )
    )

    st.divider()

    show_customer_churn(
        customer_churn_prediction(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        )
    )

    st.divider()


    inventory_for_health = pd.DataFrame(
        inventory_status(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        columns=["Product","Stock"]
    )


    show_business_health(
        total_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        total_orders(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        total_customers(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        inventory_for_health
    )

    st.divider()


    show_customer_intelligence(
        top_customers(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        )
    )

    st.divider()

    st.header("🛒 Product Recommendation Engine")

    st.caption(
        "Identifies products frequently purchased together "
        "using historical customer transaction patterns."
    )

    recommendation_data = product_recommendations(
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    )

    if recommendation_data:

        recommendation_df = pd.DataFrame(
            recommendation_data,
            columns=[
                "Product",
                "Recommended Product",
                "Purchase Frequency"
            ]
        )

        st.dataframe(
            recommendation_df,
            width="stretch",
            hide_index=True
        )

    else:

        st.info(
            "No product recommendations available."
        )

    show_recommendations(
        inventory_status(
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
        )
    )
# ===========================
# ANALYTICS
# ===========================

elif page == "📈 Analytics":

    st.sidebar.markdown("---")
    st.sidebar.markdown("## 🎯 Filters")

    country_options = ["All"] + [
        row[0] for row in available_countries()
    ]

    selected_country = st.sidebar.selectbox(
        "Country",
        country_options,
        key="analytics_country"
    )

    region_options = ["All"] + [
        row[0] for row in available_regions(selected_country)
    ]

    selected_region = st.sidebar.selectbox(
        "Region",
        region_options,
        key="analytics_region"
    )

    category_options = ["All"] + [
        row[0] for row in available_categories(
            selected_region,
            selected_country
        )
    ]

    selected_category = st.sidebar.selectbox(
        "Category",
        category_options,
        key="analytics_category"
    )

    product_options = ["All"] + [
        row[0] for row in available_products(
            selected_region,
            selected_country,
            selected_category
        )
    ]

    selected_product = st.sidebar.selectbox(
        "Product",
        product_options,
        key="analytics_product"
    )

    year_options = ["All"] + [
        int(row[0]) for row in available_years(
            selected_region,
            selected_country,
            selected_category,
            selected_product
        )
    ]

    selected_year = st.sidebar.selectbox(
        "Year",
        year_options,
        key="analytics_year"
    )

    st.title("📈 Analytics")

    st.divider()

    products_df = pd.DataFrame(
        top_products(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        columns=["Product", "Units Sold"]
    )


    customers_df = pd.DataFrame(
        top_customers(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        columns=["Customer", "Revenue"]
    )


    inventory_df = pd.DataFrame(
        inventory_status(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        columns=["Product", "Stock"]
    )

    
    st.subheader("🏆 Top Selling Products")

    search_product = st.text_input(
        "🔍 Search Product",
        key="search_product"
    )

    if search_product:
        products_df = products_df[
            products_df["Product"].str.contains(
                search_product,
                case=False
            )
        ]

    sort_order = st.selectbox(
        "Sort Products",
        [
            "Highest Sales",
            "Lowest Sales"
        ]
    )

    if sort_order == "Lowest Sales":
        products_df = products_df.sort_values(
            "Units Sold"
        )
    else:
        products_df = products_df.sort_values(
            "Units Sold",
            ascending=False
        )

    st.dataframe(
        products_df,
        width="stretch",
        hide_index=True
    )

    st.download_button(
        "⬇ Download Top Products CSV",
        products_df.to_csv(index=False),
        "top_products.csv",
        "text/csv"
    )

    st.divider()

    st.subheader("👑 Top Customers")

    search_customer = st.text_input(
        "🔍 Search Customer",
        key="search_customer"
    )

    if search_customer:
        customers_df = customers_df[
            customers_df["Customer"].str.contains(
                search_customer,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        customers_df,
        width="stretch",
        hide_index=True
    )

    st.download_button(
        "⬇ Download Top Customers CSV",
        customers_df.to_csv(index=False),
        "top_customers.csv",
        "text/csv"
    )

    st.divider()

    st.subheader("📦 Inventory Status")

    st.dataframe(
        inventory_df.style.background_gradient(
            subset=["Stock"],
            cmap="RdYlGn"
        ),
    width="stretch"
    )

    st.download_button(
    "⬇ Download Inventory CSV",
    inventory_df.to_csv(index=False),
    "inventory.csv",
    "text/csv"
    )

    st.divider()

    monthly_df = pd.DataFrame(
        monthly_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
    columns=["Month", "Revenue"]
    )

    fig_month = px.line(
        monthly_df,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue"
    )

    st.subheader("📅 Monthly Revenue")

    st.plotly_chart(
        fig_month,
        width="stretch"
    )

    st.divider()

    category_sales_df = pd.DataFrame(
        category_sales(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
    columns=["Category", "Units Sold"]
    )

    fig_sales = px.pie(
        category_sales_df,
        names="Category",
        values="Units Sold",
        title="Sales Distribution"
    )

    st.subheader("🥧 Sales Distribution")

    st.plotly_chart(
        fig_sales,
        width="stretch"
    )
     
    st.divider()

    st.subheader("🔮 Revenue Forecast")

    forecast_fig = show_forecast(
        monthly_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        )
    )

    if forecast_fig:
        st.plotly_chart(
            forecast_fig,
            width="stretch"
        )

# ===========================
# RECOMMENDATIONS
# ===========================

elif page == "💡 Recommendations":

    st.title("💡 Business Recommendations")

    st.divider()

    inventory = inventory_status()

    show_recommendations(
        inventory
    )

    st.divider()

    if total_revenue() > 5000000:
        st.success("✅ Revenue is performing very well.")
    else:
        st.warning("⚠ Revenue can be improved.")

    if total_orders() < 30:
        st.warning(
            "⚠ Order volume is relatively low. Consider promotional campaigns."
        )
    else:
        st.success("✅ Order volume is healthy.")

    low_stock = [
        item[0]
        for item in inventory
        if item[1] < 50
    ]

    if low_stock:
        st.error("Low Stock Products:")

        for product in low_stock:
            st.write(f"• {product}")

    else:
        st.success("✅ No products are running low on stock.")


st.divider()

st.markdown(
    """
    <div style='text-align:center;'>

    **Decision Intelligence Platform**

    Powered by Python • PostgreSQL • Streamlit • Plotly

    © 2026 Raunaq Ghosh

    </div>
    """,
    unsafe_allow_html=True
)
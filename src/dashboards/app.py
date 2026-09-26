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
from components.filters import create_filter_sidebar

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Decision Intelligence Platform",
    page_icon="📊",
    layout="wide"
)


st.markdown(
    """
    <style>
    #stDecoration {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

from analytics.sales_queries import(
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

    with st.sidebar:
        selected_region, selected_country, selected_category, selected_product, selected_year = create_filter_sidebar(
            "dash",
            available_regions,
            available_countries,
            available_categories,
            available_products,
            available_years,
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
        )
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
        use_container_width=True
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
            use_container_width=True
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
        use_container_width=True
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
            use_container_width=True
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
            use_container_width=True
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
            use_container_width=True
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

        # ============================================================
    # PRODUCT AFFINITY & RECOMMENDATIONS
    # ============================================================

    st.header("🛍️ Product Affinity & Recommendations")

    st.caption(
        "Identifies products frequently purchased together "
        "to uncover cross-selling opportunities from historical "
        "customer transaction patterns."
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
                "Frequently Purchased Together",
                "Purchase Frequency"
            ]
        )

        # --------------------------------------------------------
        # TOP PRODUCT ASSOCIATIONS
        # --------------------------------------------------------

        st.subheader("📊 Top Product Associations")

        chart_df = recommendation_df.copy()

        chart_df["Association"] = (
            chart_df["Product"]
            + " → "
            + chart_df["Frequently Purchased Together"]
        )

        chart_df = chart_df.sort_values(
            "Purchase Frequency",
            ascending=True
        )

        fig_recommendations = px.bar(
            chart_df,
            x="Purchase Frequency",
            y="Association",
            orientation="h",
            text="Purchase Frequency",
            title="Frequently Purchased Product Pairs"
        )

        fig_recommendations.update_layout(
            template="plotly_dark",
            height=500,
            xaxis_title="Purchase Frequency",
            yaxis_title="",
            showlegend=False
        )

        fig_recommendations.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig_recommendations,
            use_container_width=True
        )

        # --------------------------------------------------------
        # DETAILED RECOMMENDATIONS
        # --------------------------------------------------------

        st.subheader("📋 Detailed Recommendations")

        st.dataframe(
            recommendation_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No product recommendations available for the selected filters."
        )
# ===========================
# ANALYTICS
# ===========================

elif page == "📈 Analytics":

    with st.sidebar:
        selected_region, selected_country, selected_category, selected_product, selected_year = create_filter_sidebar(
            "an",
            available_regions,
            available_countries,
            available_categories,
            available_products,
            available_years,
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

    # --------------------------------------------------------
    # PRODUCT CONTROLS
    # --------------------------------------------------------

    sort_col, download_col = st.columns([2, 1])

    with sort_col:
        sort_order = st.selectbox(
            "Sort by",
            [
                "Highest Sales",
                "Lowest Sales"
            ],
            key="analytics_product_sort"
        )

    if sort_order == "Lowest Sales":
        products_df = products_df.sort_values(
            "Units Sold",
            ascending=True
        )
    else:
        products_df = products_df.sort_values(
            "Units Sold",
            ascending=False
        )

    with download_col:
        st.write("")
        st.download_button(
            "⬇ Download CSV",
            products_df.to_csv(index=False),
            "top_products.csv",
            "text/csv",
            use_container_width=True
        )

    # --------------------------------------------------------
    # PRODUCT TABLE
    # --------------------------------------------------------

    st.dataframe(
        products_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Product": st.column_config.TextColumn(
                "Product"
            ),
            "Units Sold": st.column_config.NumberColumn(
                "Units Sold",
                format="%,.0f"
            )
        }
    )

    st.divider()

    st.subheader("👑 Top Customers")

    customer_sort_col, customer_download_col = st.columns([2, 1])

    with customer_sort_col:
        customer_sort_order = st.selectbox(
            "Sort by",
            [
                "Highest Revenue",
                "Lowest Revenue"
            ],
            key="analytics_customer_sort"
        )

    if customer_sort_order == "Lowest Revenue":
        customers_df = customers_df.sort_values(
            "Revenue",
            ascending=True
        )
    else:
        customers_df = customers_df.sort_values(
            "Revenue",
            ascending=False
        )

    with customer_download_col:
        st.write("")
        st.download_button(
            "⬇ Download CSV",
            customers_df.to_csv(index=False),
            "top_customers.csv",
            "text/csv",
            use_container_width=True
        )

    st.dataframe(
        customers_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Customer": st.column_config.TextColumn(
                "Customer"
            ),
            "Revenue": st.column_config.NumberColumn(
                "Revenue",
                format="%,.2f"
            )
        }
    )

    st.divider()

    st.subheader("📦 Inventory Status")

    st.dataframe(
        inventory_df.style.background_gradient(
            subset=["Stock"],
            cmap="RdYlGn"
        ),
        use_container_width=True
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
        use_container_width=True
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
        use_container_width=True
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
            use_container_width=True
        )

# ===========================
# RECOMMENDATIONS
# ===========================

elif page == "💡 Recommendations":

    with st.sidebar:
        selected_region, selected_country, selected_category, selected_product, selected_year = create_filter_sidebar(
            "rec",
            available_regions,
            available_countries,
            available_categories,
            available_products,
            available_years,
        )

    st.title("💡 Business Recommendations")

    st.divider()

    inventory = inventory_status(
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    )

    show_recommendations(
        inventory
    )

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
        inventory,
        columns=["Product", "Stock"]
    )

    show_executive_insights(
        total_revenue(
            selected_region,
            selected_country,
            selected_category,
            selected_product,
            selected_year
        ),
        products_df,
        inventory_df,
        customers_df
    )

    st.divider()

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

        # ============================================================
    # DYNAMIC RECOMMENDED ACTIONS
    # ============================================================

    st.subheader("📌 Recommended Actions")

    recommendation_actions = []

    # ------------------------------------------------------------
    # 1. LOW STOCK
    # ------------------------------------------------------------

    low_stock = [
        (product, stock)
        for product, stock in inventory
        if stock < 50
    ]

    if low_stock:

        low_stock_product, low_stock_value = min(
            low_stock,
            key=lambda x: x[1]
        )

        recommendation_actions.append(
            f"📦 Increase inventory for **{low_stock_product}**, "
            f"which currently has only **{low_stock_value} units** in stock."
        )

    else:

        recommendation_actions.append(
            "✅ Inventory levels are currently healthy for the selected filters."
        )

    # ------------------------------------------------------------
    # 2. SLOW-MOVING PRODUCT
    # ------------------------------------------------------------

    if not products_df.empty:

        slow_product = products_df.sort_values(
            "Units Sold",
            ascending=True
        ).iloc[0]

        recommendation_actions.append(
            f"🐢 Review sales strategy for **{slow_product['Product']}**, "
            f"which has the lowest sales volume among the top products "
            f"with **{slow_product['Units Sold']} units sold**."
        )

    # ------------------------------------------------------------
    # 3. HIGH-VALUE CUSTOMER
    # ------------------------------------------------------------

    if not customers_df.empty:

        top_customer = customers_df.sort_values(
            "Revenue",
            ascending=False
        ).iloc[0]

        recommendation_actions.append(
            f"👑 Consider loyalty offers for **{top_customer['Customer']}**, "
            f"the highest-value customer in the selected dataset "
            f"with revenue of **₹{top_customer['Revenue']:,.2f}**."
        )

    # ------------------------------------------------------------
    # 4. HIGH-PERFORMING REGION
    # ------------------------------------------------------------

    region_data = revenue_by_region(
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    )

    if region_data:

        region_df = pd.DataFrame(
            region_data,
            columns=["Region", "Revenue"]
        )

        if not region_df.empty:

            top_region = region_df.sort_values(
                "Revenue",
                ascending=False
            ).iloc[0]

            recommendation_actions.append(
                f"📍 Focus marketing attention on **{top_region['Region']}**, "
                f"which generated the highest revenue of "
                f"**₹{top_region['Revenue']:,.2f}** for the selected filters."
            )

    # ------------------------------------------------------------
    # 5. MONTHLY REVENUE TREND
    # ------------------------------------------------------------

    monthly_data = monthly_revenue(
        selected_region,
        selected_country,
        selected_category,
        selected_product,
        selected_year
    )

    if monthly_data:

        monthly_df = pd.DataFrame(
            monthly_data,
            columns=["Month", "Revenue"]
        )

        if len(monthly_df) >= 2:

            latest_revenue = monthly_df.iloc[-1]["Revenue"]
            previous_revenue = monthly_df.iloc[-2]["Revenue"]

            if previous_revenue != 0:

                revenue_change = (
                    (latest_revenue - previous_revenue)
                    / previous_revenue
                ) * 100

                if revenue_change < -10:

                    recommendation_actions.append(
                        f"⚠️ Investigate the recent revenue decline: "
                        f"revenue decreased by **{abs(revenue_change):.1f}%** "
                        f"from the previous month."
                    )

                elif revenue_change > 10:

                    recommendation_actions.append(
                        f"📈 Monitor the recent growth trend: "
                        f"revenue increased by **{revenue_change:.1f}%** "
                        f"from the previous month."
                    )

                else:

                    recommendation_actions.append(
                        f"📊 Revenue is relatively stable, changing by "
                        f"**{revenue_change:+.1f}%** compared with the previous month."
                    )

    # ------------------------------------------------------------
    # DISPLAY
    # ------------------------------------------------------------

    if recommendation_actions:

        st.markdown("### Priority Actions")

        for action in recommendation_actions:
            st.markdown(f"- {action}")

    else:

        st.info(
            "No specific recommendations are available for the selected filters."
        )

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
# 📊 Decision Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Supabase](https://img.shields.io/badge/Supabase-Cloud-3ECF8E)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-6A5ACD)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive **Decision Intelligence Platform for Retail Sales Analytics**, built using **Python, PostgreSQL, Supabase, Streamlit, Plotly, and Pandas**.

The platform transforms synthetic retail transaction data into a decision-support system through interactive dashboards, analytics, forecasting, customer intelligence, inventory monitoring, and automated recommendations.

> **Note:** This is a portfolio/demo project simulating a retail analytics platform. All data is synthetically generated using Faker to model realistic sales, customer, and inventory patterns — it is not connected to a live business.

---

# 📖 About This Project

Most retail businesses generate large volumes of transactional data — orders, customers, inventory, regional sales — but that data is only useful if it can be turned into decisions. This project explores exactly that pipeline: taking raw relational data and turning it into an executive-facing decision-support tool, end to end.

The development followed three major layers:

**1. Data Foundation** — Designed a normalized PostgreSQL schema (customers, orders, order items, products, categories, regions, countries) and generated synthetic data using Faker to simulate retail relationships and business scenarios (seasonal revenue patterns, repeat customers, regional variance, stock levels).

**2. Analytics Layer** — Built a Python analytics module (`analytics/sales_queries.py`) responsible for all business logic: revenue aggregation, customer segmentation (quantile-based bucketing), churn prediction, anomaly detection, and recommendation generation — all backed by parameterized SQL queries rather than pulling raw tables into Pandas and filtering in memory.

**3. Presentation Layer** — Built a multi-page Streamlit application with cascading filters (Country → Region → Category → Product → Year), Plotly visualizations styled consistently across the dashboard, and a componentized structure (`components/`) so each dashboard section — KPIs, charts, forecasts, segmentation — is independently maintainable.

Throughout development, the project went through several rounds of debugging and refinement, including:
- Fixing chart axis rendering issues caused by mismatched tick configurations (`dtick` used incorrectly on categorical axes)
- Correcting category ordering logic in customer segmentation, which was previously sorting by frequency instead of business logic (Low Value → Regular → VIP)
- Catching and resolving a page-routing bug where a UI label and its corresponding navigation condition fell out of sync
- Auditing the underlying data for referential integrity issues (e.g., a product incorrectly linked to the wrong category)

This iterative hardening is part of why the project is structured the way it is now — the goal wasn't just "does it run," but "does it behave correctly across real filter combinations."

---

# 🎯 Project Objective

The Decision Intelligence Platform demonstrates how raw transactional data can be converted into structured insights that support business monitoring, analysis, and decision-making.

The application combines:

- PostgreSQL Relational Database
- Supabase Cloud Database
- Streamlit Web Application
- Plotly Interactive Visualizations
- Python Analytics Modules

to provide an end-to-end workflow from raw transactional data to business-oriented insights.

---

# 🏗 System Architecture

The platform follows a layered architecture, separating data generation, storage, business logic, and presentation:

```mermaid
flowchart TD
    A[Faker Data Generator] --> B[(PostgreSQL Database - Hosted on Supabase)]

    B --> C[Analytics Layer - sales_queries.py]
    C --> C1[Revenue and KPI Queries]
    C --> C2[Customer Segmentation and Churn]
    C --> C3[Forecasting and Anomaly Detection]
    C --> C4[Recommendation Logic]

    C1 --> D[Streamlit App - app.py]
    C2 --> D
    C3 --> D
    C4 --> D

    D --> E[Component Layer - components]
    E --> F[Plotly Visualizations]
    E --> G[KPI Cards and Tables]

    F --> H[Executive Dashboard]
    G --> H
    F --> I[Analytics Dashboard]
    G --> I
    D --> J[Business Recommendations Interface]
```

**How data flows through the system:**

1. **Generation** — `generators/` uses Faker to populate customers, orders, products, categories, regions, and countries with relationally-consistent synthetic data.
2. **Storage** — Data lives in a normalized PostgreSQL schema hosted on Supabase, with foreign-key relationships across orders → customers → regions → countries and order items → products → categories.
3. **Query & Business Logic** — `analytics/sales_queries.py` exposes parameterized functions (e.g. `total_revenue()`, `available_products()`, `customer_segmentation()`) that build filtered SQL queries based on the user's active Country / Region / Category / Product / Year selections — filtering happens in the database, not after loading full tables into memory.
4. **Presentation** — `src/dashboards/app.py` orchestrates page routing (Dashboard / Analytics / Recommendations) and passes query results into individual `components/*.py` modules, each responsible for rendering one self-contained section (KPI cards, charts, segmentation, forecasts, recommendations).
5. **Visualization** — Plotly renders all charts with a consistent dark theme, explicit axis/tick configuration, and category ordering, so visual output stays stable regardless of what filter combination the user selects.

This separation means the SQL/business logic layer can be tested or reused independently of the UI, and new dashboard sections can be added as new components without touching the core query layer.

---

# 🚀 Features

### 📌 Executive Dashboard

- Executive KPI Cards
- Executive Summary
- Revenue Analysis
- Inventory Status
- Business Insights

### 📊 Advanced Analytics

- Product Performance Analysis
- Customer Performance Analysis
- Monthly Revenue Trend
- Revenue Forecasting
- Revenue Anomaly Detection
- Customer Segmentation
- Customer Churn Prediction
- Customer Revenue Intelligence
- Business Health Score
- Sales Distribution
- Product Recommendation Engine
- Automated Business Recommendations

### 🎛 Interactive Filtering

- Country
- Region
- Category
- Product
- Year

---

# 🌐 Live Demo

https://decision-intelligence-platform-cw5a5vt8dvjnyyzukqmeor.streamlit.app/

---

# 📸 Dashboard Preview

## Executive Dashboard

### Executive Overview

![Executive Overview](screenshots/dashboard_executive_overview.png)

### Executive Summary

![Executive Summary](screenshots/dashboard_executive_summary.png)

### Revenue Analysis

![Revenue Analysis](screenshots/dashboard_revenue_analysis.png)

### Inventory Status

![Inventory Status](screenshots/dashboard_inventory_status.png)

### Business Insights

![Business Insights](screenshots/dashboard_business_insights.png)

---

## Analytics Dashboard

### Product & Customer Analysis

![Product Customer Analysis](screenshots/analytics_product_customer_analysis.png)

### Top Selling Products

![Top Selling Products](screenshots/analytics_top_selling_products.png)

### Top Customers

![Top Customers](screenshots/analytics_top_customers.png)

### Monthly Revenue Trend

![Monthly Revenue](screenshots/analytics_monthly_revenue_trend.png)

### Revenue Forecast

![Revenue Forecast](screenshots/analytics_revenue_forecast.png)

### Revenue Anomaly Detection

![Revenue Anomaly](screenshots/analytics_revenue_anomaly.png)

### Sales Distribution

![Sales Distribution](screenshots/analytics_sales_category_distribution.png)

### Customer Segmentation

![Customer Segmentation](screenshots/analytics_customer_segmentation.png)

### Customer Churn Prediction

![Customer Churn](screenshots/analytics_customer_churn_prediction.png)

### Customer Revenue Distribution

![Customer Revenue](screenshots/analytics_customer_revenue_distribution.png)

### Business Health & Customer Intelligence

![Business Health](screenshots/analytics_business_health_customer_intelligence.png)

### Product Recommendation Engine

![Recommendation Engine](screenshots/analytics_product_recommendation_engine.png)

### Automated Business Recommendations

![Business Recommendations](screenshots/analytics_automated_business_recommendations.png)

---

# 🗄 Database Architecture

### Supabase Database

![Supabase](screenshots/analytics_supabase_database.png)

### Database Schema

![Database Schema](screenshots/analytics_supabase_schema.png)

### PostgreSQL Query Analysis

![PostgreSQL](screenshots/analytics_postgresql_query_analysis.png)

---

# 💻 Project Architecture

### VS Code Project Structure

![VS Code](screenshots/analytics_vscode_project_structure.png)

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| PostgreSQL | Relational Database |
| Supabase | Cloud Database |
| Streamlit | Interactive Dashboard |
| Plotly | Data Visualization |
| Pandas | Data Analysis |
| SQL | Query Processing |
| Faker | Synthetic Data Generation |
| Streamlit Cloud | Application Deployment |

---

# 🧠 Skills Demonstrated

- Relational Database Design
- Data Modeling & Relational Schema Design
- Synthetic Data Generation
- SQL Query Development & Optimization
- PostgreSQL & Supabase Integration
- Python Data Analytics
- Business Intelligence Development
- Streamlit Application Development
- Interactive Data Visualization
- Customer Analytics
- Forecasting & Anomaly Detection
- Data Quality Validation
- Git & GitHub Workflow

---

# 📂 Project Structure

```
Decision_Intelligence_Platform
│
├── data
├── docs
├── notebooks
├── reports
├── screenshots
├── sql
├── src
│   ├── analytics
│   ├── components
│   ├── dashboards
│   ├── database
│   ├── generators
│   └── utils
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ▶ Installation

Clone the repository

```bash
git clone https://github.com/ghoshraunaq-art/Decision-Intelligence-Platform.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
python -m streamlit run src/dashboards/app.py
```

---

# 📈 Future Improvements

- ML-based Demand Forecasting
- Customer Lifetime Value Prediction
- Advanced RFM Segmentation
- Profit & Margin Analysis
- Automated Data Pipeline Integration
- Real-Time Data Streaming
- Authentication & Role-Based Access Control
- Exportable Business Reports (PDF / Excel)
- AI-Assisted Business Insights Generation

---

# 📌 Disclaimer

This project is developed for educational and portfolio purposes.

The dataset used in this platform is synthetically generated using Faker and does not represent any real company's sales, customers, or inventory information.

---

# 👨‍💻 Author

**Raunaq Ghosh**

B.Tech Computer Science & Engineering

Kalinga Institute of Industrial Technology (KIIT)

Bhubaneswar, Odisha, India

---

⭐ If you found this project useful, consider giving it a star.




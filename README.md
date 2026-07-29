![Python](https://img.shields.io/badge/Python-3.x-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![License](https://img.shields.io/badge/License-MIT-green)

# Python PostgreSQL Streamlit Plotly

# 📊 Decision Intelligence Platform

An interactive **Business Intelligence and Analytics Dashboard** built using **Python, PostgreSQL, Streamlit and Plotly**.

The platform analyzes retail sales data and provides actionable business insights through interactive dashboards, KPIs, analytics modules, inventory monitoring, customer intelligence and recommendation systems.

---

# 🎯 Project Objective

The **Decision Intelligence Platform** is designed to help businesses analyze retail transaction data and make data-driven decisions.

The system integrates:

- Sales analytics
- Customer behaviour analysis
- Product performance monitoring
- Inventory intelligence
- Revenue trend analysis
- Business recommendations

The platform uses a normalized PostgreSQL database with Streamlit-based interactive visualization to deliver an end-to-end business analytics solution.

---

# 🚀 Features

## 📊 Executive Dashboard

- Executive KPI Dashboard
- Total Revenue Analysis
- Products Sold Tracking
- Customer and Order Metrics
- Revenue by Category
- Revenue by Region
- Interactive Filters:
  - Country
  - Region
  - Category
  - Product
  - Year
- Top Selling Products
- Top Customers
- Monthly Revenue Trends
- Sales Distribution Analysis


---

# 📈 Advanced Analytics

## Revenue Intelligence

- Monthly Revenue Analysis
- Revenue Trend Forecast Visualization
- Revenue Anomaly Detection


## Customer Intelligence

- Customer Segmentation
- Customer Purchase Behaviour Analysis
- Customer Churn Risk Analysis
- Highest Value Customer Identification


## Inventory Intelligence

- Inventory Monitoring
- Low Stock Detection
- Inventory Risk Analysis


## Business Intelligence

- Business Health Score
- Automated Business Insights
- Strategic Recommendations

---

# 🛒 Recommendation System

## Product Recommendation Engine

The system identifies products frequently purchased together by analyzing historical customer transaction patterns.

The recommendation module helps businesses:

- Understand product relationships
- Improve cross-selling opportunities
- Design better product bundles


## Inventory-Based Recommendations

Generates recommendations based on:

- Low inventory products
- Stock risk conditions
- Product demand patterns

---

# 🌐 Live Demo

Streamlit Cloud Deployment:

https://decision-intelligence-platform-cw5a5vt8dvjnyyzukqmeor.streamlit.app/

---

# 🛠 Tech Stack

## Programming Language

- Python


## Database

- PostgreSQL
- Supabase


## Data Processing

- Pandas
- Faker


## Visualization

- Streamlit
- Plotly


## Query Language

- SQL

---

# ☁️ Deployment Architecture

| Component | Technology |
|-|-|
| Frontend Dashboard | Streamlit Cloud |
| Database | PostgreSQL (Supabase) |
| Visualization | Plotly |
| Data Processing | Python + Pandas |
| Backend Queries | SQL |

---

# 🗄 Database Design

The project uses a normalized relational PostgreSQL database.

## Main Tables

- Customers
- Countries
- Regions
- Categories
- Brands
- Products
- Inventory
- Orders
- Order Items
- Sales


The database follows relational database principles with foreign key relationships to maintain data consistency.

## Database Architecture

The system follows an analytical database structure:

### Fact Table

- Sales

### Dimension Tables

- Customers
- Products
- Categories
- Brands
- Regions
- Countries

This structure allows efficient analytical queries and dashboard reporting.

---

# 📈 Dashboard Modules

## Dashboard

Includes:

- Revenue KPIs
- Executive Summary
- Revenue Category Analysis
- Regional Performance Analysis
- Product Performance
- Customer Performance
- Inventory Status
- Monthly Revenue Analysis
- Sales Distribution
- Revenue Forecast
- Revenue Anomaly Detection
- Customer Intelligence
- Business Health Score
- Product Recommendation Engine


---

## Analytics

Includes:

- Product Analysis
- Customer Segmentation
- Customer Churn Risk Analysis
- Inventory Analysis
- Revenue Analysis


---

## Recommendations

Provides:

- Product purchase pattern recommendations
- Inventory-based business suggestions
- Low stock alerts

---

# 📂 Project Structure

```
Decision_Intelligence_Platform/

│
├── src/
│
│   ├── analytics/
│   │
│   ├── components/
│   │
│   ├── dashboards/
│   │
│   ├── database/
│   │
│   ├── insert_data/
│
├── requirements.txt
│
└── README.md
```

---

# 📷 Project Screenshots

The repository contains screenshots demonstrating:

- Executive Dashboard
- Analytics Modules
- Recommendation Engine
- PostgreSQL Database Schema
- Supabase Database Deployment
- Streamlit Cloud Deployment

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/ghoshraunaq-art/Decision-Intelligence-Platform.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Dashboard

```bash
python -m streamlit run src/dashboards/app.py
```

---

# 📌 Future Improvements

Future enhancements include:

- Machine Learning based demand forecasting
- Advanced RFM customer analytics
- Profit and margin analysis
- Automated PDF/Excel dashboard reports
- User authentication system
- Role-based dashboard access
- Real-time sales data integration
- Automated email/SMS business alerts
- Advanced predictive analytics models

---

# 👨‍💻 Author

**Raunaq Ghosh**

B.Tech Computer Science & Engineering  
Kalinga Institute of Industrial Technology (KIIT)  
Bhubaneswar, Odisha, India


GitHub:

https://github.com/ghoshraunaq-art


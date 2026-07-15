# 📊 Decision Intelligence Platform

An interactive Business Intelligence Dashboard built using **Python, PostgreSQL, Streamlit and Plotly**.

The project analyzes retail sales data and provides real-time business insights through KPIs, charts, analytics and recommendations.

---

## 🚀 Features

* Executive KPI Dashboard
* Revenue by Category
* Revenue by Region
* Region-wise Filtering
* Top Selling Products
* Top Customers
* Monthly Revenue Trend
* Inventory Monitoring
* Sales Distribution
* Business Recommendations

---

## 🌐 Live Demo

https://decision-intelligence-platform-cw5a5vt8dvjnyyzukqmeor.streamlit.app/

---

## 🛠 Tech Stack

* Python
* PostgreSQL
* Streamlit
* Plotly
* Pandas
* Faker
* SQL

---

## ☁️ Deployment

- **Frontend:** Streamlit Cloud
- **Database:** PostgreSQL (Supabase)
- **Visualization:** Plotly
- **Programming Language:** Python

---

## 🗄 Database Design

The project uses a normalized PostgreSQL database.

Main tables:

* Customers
* Countries
* Regions
* Categories
* Products
* Inventory
* Orders
* Order Items
* Sales

The tables are connected using foreign keys to maintain relational integrity.

---

## 📈 Dashboard Modules

### Dashboard

* Revenue KPIs
* Executive Summary
* Revenue by Category
* Revenue by Region
* Top Products
* Top Customers
* Inventory Status
* Monthly Revenue
* Sales Distribution

### Analytics

* Product Performance
* Customer Performance
* Inventory Analysis
* Monthly Revenue Trend

### Recommendations

Automatically generates business recommendations using sales and inventory data.

---

## 📂 Project Structure

```text
Decision_Intelligence_Platform/
│
├── src/
│   ├── analytics/
│   ├── components/
│   ├── dashboards/
│   ├── database/
│   ├── insert_data/
│   └── ...
│
├── requirements.txt
└── README.md
```

---

## 📷 Project Screenshots

The repository contains screenshots demonstrating:

- Executive Dashboard
- Analytics Dashboard
- Recommendations Dashboard
- PostgreSQL Database (pgAdmin)
- Supabase Database Configuration
- Streamlit Cloud Deployment

---

## 🎯 Project Objective

The Decision Intelligence Platform is designed to help businesses analyze retail sales data and make informed decisions through interactive dashboards, KPIs, visual analytics, inventory monitoring, and automated business recommendations.

The platform integrates PostgreSQL, Supabase, Streamlit, and Plotly to provide a cloud-based analytics solution capable of delivering actionable business insights in real time.

---

## ▶️ Installation

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

## 📌 Future Improvements

- Machine Learning Sales Forecasting
- Customer Segmentation using RFM Analysis
- Profit and Margin Analysis
- Export Dashboard Reports (PDF/Excel)
- User Authentication & Login System
- Role-Based Dashboard Access
- Real-Time Sales Data Integration
- AI-powered Business Insights
---

## 👨‍💻 Author

**Raunaq Ghosh**

B.Tech Computer Science & Engineering  
Kalinga Institute of Industrial Technology (KIIT)  
Bhubaneswar, Odisha, India

GitHub:
https://github.com/ghoshraunaq-art

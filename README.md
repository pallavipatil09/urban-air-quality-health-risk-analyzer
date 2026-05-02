# 🌍 Urban Air Quality & Health Risk Analyzer  
📊 *End-to-End Data Analytics Project | Environment + Health Insights*

![Python](https://img.shields.io/badge/Python-Data%20Analysis-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Project](https://img.shields.io/badge/Project-End--to--End-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🚀 Summary  
Developed a complete **data analytics pipeline** to analyze the relationship between **air pollution, weather conditions, and respiratory health risks** across major Indian cities.

The project integrates **multiple real-world datasets** and delivers **actionable insights through EDA and an interactive Power BI dashboard**.

---

## 📌 Project Overview  

This project combines:

- 🌫️ **Air Quality Data (AQI)**
- 🌡️ **Weather Data (Temperature, Humidity)**
- 🏥 **Health Data (Respiratory Cases)**  

👉 Objective: Understand how environmental factors impact **public health risk** and identify **high-risk cities and seasons**

---

## 🎯 Key Objectives

- Analyze AQI trends across cities  
- Compare pollution levels by **city and season**  
- Study correlation between **AQI and respiratory cases**  
- Build an **interactive Power BI dashboard**  
- Generate **data-driven insights for decision-making**  

---

## 🛠️ Tools & Technologies  

| Tool | Purpose |
|------|--------|
| 🐍 Python (Pandas) | Data Cleaning & Transformation |
| 📊 Matplotlib & Seaborn | Data Visualization (EDA) |
| 📈 Power BI | Dashboard Development |
| ⚡ DAX | KPI Calculations |
| 💻 VS Code | Development Environment |

---

## 📂 Project Structure  

```text
aqi_health_project/
│── data/
│   ├── raw/
│   └── clean/
│
│── notebooks/
│   ├── get_aqi_data.py
│   ├── get_weather_data.py
│   ├── get_hospital_data.py
│   ├── clean_merge_data.py
│   └── eda_analysis.py
│
│── outputs/
│   ├── dashboard.png
│   ├── aqi_trend.png
│   ├── correlation_heatmap.png
│   ├── aqi_vs_health_impact.png
│   ├── seasonal_aqi_analysis.png
│   └── top_polluted_cities.png
│
│── dashboard/
│   └── Urban_Air_Quality_Health_Risk_Analyzer.pbix
│
│── README.md
```
---

## 📊 Dataset Columns

- city
- date
- aqi
- temperature
- humidity
- respiratory_cases
- aqi_category_month
- month_number
- season
- health_risk_score

---

## 📸 Dashboard Preview
<img width="1325" height="738" alt="aqi_dashboard" src="https://github.com/user-attachments/assets/fde0ea6b-2532-4c6e-b871-2a31b04369d6" />

---

## 🔍 Exploratory Data Analysis (EDA)

- AQI Trend by City
- Top Polluted Cities
- Respiratory Cases by City
- AQI vs Respiratory Cases
- Correlation Heatmap
- Seasonal AQI Analysis
- Monthly Pollution Patterns

---

## 📈 Dashboard Features

### KPI Cards

- Total Cities Tracked
- Avg AQI
- Total Respiratory Cases
- Avg Health Risk Score
- Monthly AQI Change %

### Visuals

- AQI Trend Line Chart
- Top Polluted Cities Bar Chart
- Respiratory Cases Chart
- AQI vs Health Impact Scatter Plot
- City Air Quality Map

### Filters / Slicers

- City
- Season
- AQI Category

---

## 📈 Key Insights

- 🔴 Higher AQI is strongly associated with increased respiratory cases
- ❄️ Winter season shows peak pollution levels
- 🌧️ Monsoon improves air quality significantly
- 🏙️ Cities like Delhi, Lucknow, and Jaipur are high-risk zones
- 📊 Health Risk Score simplifies complex environmental data into one KPI

---

## 🎯 Business Impact

✔ Identify high-risk cities and seasons
✔ Support public health decision-making
✔ Enable environmental policy insights
✔ Improve awareness of pollution-health linkage

---

## 🚀 How to Run

### 1. Install Required Libraries

```bash
pip install pandas matplotlib seaborn openpyxl
```

### 2. Run Python Files

```bash
python notebooks/get_aqi_data.py
python notebooks/get_weather_data.py
python notebooks/get_hospital_data.py
python notebooks/clean_merge_data.py
python notebooks/eda_analysis.py
```

### 3. Open Dashboard

Open this file in **Power BI Desktop**:

```text
dashboard/Urban_Air_Quality_Health_Risk_Analyzer.pbix
```

---

## 📌 Skills Demonstrated

- Data Cleaning
- Data Transformation
- Exploratory Data Analysis
- Dashboard Design
- DAX Measures
- Data Storytelling
- Business Insights
  
---

## 🏆 Project Highlights
- End-to-end data analytics workflow
- Multi-source data integration
- Real-world problem solving
- Insight-driven dashboard
- Clean and scalable project structure

---

## 👩‍💻 Author  
**Pallavi Patil**  
Aspiring Data Analyst | SQL | Excel | Power BI | Python | Tableau

---

## 📬 Connect With Me  
- LinkedIn: www.linkedin.com/in/patilpallavianil

---

## ⭐ If you like this project  
Give it a ⭐ and share your feedback!


# urban-air-quality-health-risk-analyzer

## 📌 Overview

An end-to-end Data Analytics project that analyzes the relationship between **air pollution, weather conditions, and respiratory health risks** across major Indian cities.

The project combines AQI, temperature, humidity, and respiratory case data using **Python, Pandas, EDA, Power BI, and DAX** to generate meaningful insights and an interactive dashboard.

---

## 🎯 Objectives

* Analyze AQI trends across cities
* Compare pollution levels by city and season
* Study health impact using respiratory cases
* Build an interactive Power BI dashboard
* Generate actionable insights

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Power BI
* DAX
* VS Code

---

## 📂 Project Structure

```text
aqi_health_project/
│── data/
│   ├── clean/
│   └── raw/
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
│   ├── distribution_plot.png
│   ├── monthly_heatmap.png
│   ├── seasonal_aqi_analysis.png
│   ├── top_polluted_cities.png
│   ├── pairplot.png
│
│── dashboard/
│   └── Urban_Air_Quality_Health_Risk_Analyzer.pbix
│
│── README.md
```

---

## 📊 Dataset Columns

* city
* date
* aqi
* temperature
* humidity
* respiratory_cases
* aqi_category
* month
* month_number
* season
* health_risk_score

---

## 🔍 Exploratory Data Analysis (EDA)

* AQI Trend by City
* Top Polluted Cities
* Respiratory Cases by City
* AQI vs Respiratory Cases
* Correlation Heatmap
* Seasonal AQI Analysis
* Monthly Pollution Patterns

---

## 📈 Dashboard Features

### KPI Cards

* Total Cities Tracked
* Avg AQI
* Total Respiratory Cases
* Avg Health Risk Score
* Monthly AQI Change %

### Visuals

* AQI Trend Line Chart
* Top Polluted Cities Bar Chart
* Respiratory Cases Chart
* AQI vs Health Impact Scatter Plot
* City Air Quality Map

### Filters / Slicers

* City
* Season
* AQI Category

---

## 💡 Key Insights

* Higher AQI is linked with more respiratory cases.
* Winter months show worse pollution levels.
* Delhi, Lucknow, and Jaipur are among the most polluted cities.
* Monsoon season improves air quality in many cities.
* Health Risk Score summarizes environmental risk in one KPI.

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

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* Dashboard Design
* DAX Measures
* Data Storytelling
* Business Insights



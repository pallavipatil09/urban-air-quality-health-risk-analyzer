import pandas as pd
import random

cities = {
    "Delhi": 5200,
    "Mumbai": 4100,
    "Pune": 2800,
    "Chennai": 3000,
    "Kolkata": 3900,
    "Bengaluru": 2500,
    "Hyderabad": 2700,
    "Ahmedabad": 2600,
    "Jaipur": 2400,
    "Lucknow": 3500
}

months = pd.date_range(start="2025-01-01", periods=12, freq="MS")

rows = []

for city, base_cases in cities.items():
    for date in months:
        month = date.month

        if month in [11, 12, 1, 2]:
            health_effect = 500
        elif month in [6, 7, 8, 9]:
            health_effect = -250
        else:
            health_effect = 100

        rows.append({
            "city": city,
            "date": date.strftime("%Y-%m-%d"),
            "respiratory_cases": max(100, base_cases + health_effect + random.randint(-250, 250))
        })

df = pd.DataFrame(rows)
df.to_csv("data/raw/hospital_data.csv", index=False)

print("Monthly hospital data saved!")
print("Total Rows:", len(df))
print(df.head())
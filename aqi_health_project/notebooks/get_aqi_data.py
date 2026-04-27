import pandas as pd
import random

cities = {
    "Delhi": 280,
    "Mumbai": 150,
    "Pune": 130,
    "Chennai": 110,
    "Kolkata": 190,
    "Bengaluru": 95,
    "Hyderabad": 120,
    "Ahmedabad": 170,
    "Jaipur": 210,
    "Lucknow": 240
}

months = pd.date_range(start="2025-01-01", periods=12, freq="MS")

rows = []

for city, base_aqi in cities.items():
    for date in months:
        month = date.month

        # Seasonal AQI effect
        if month in [11, 12, 1, 2]:
            seasonal_effect = 40
        elif month in [6, 7, 8, 9]:
            seasonal_effect = -25
        else:
            seasonal_effect = 5

        aqi = max(20, base_aqi + seasonal_effect + random.randint(-25, 25))

        rows.append({
            "city": city,
            "date": date.strftime("%Y-%m-%d"),
            "aqi": aqi
        })

df = pd.DataFrame(rows)
df.to_csv("data/raw/aqi_data.csv", index=False)

print("Monthly AQI data saved!")
print("Total Rows:", len(df))
print(df.head())
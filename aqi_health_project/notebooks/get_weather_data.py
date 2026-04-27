import pandas as pd
import random

cities = {
    "Delhi": (30, 45),
    "Mumbai": (29, 70),
    "Pune": (27, 55),
    "Chennai": (31, 68),
    "Kolkata": (30, 72),
    "Bengaluru": (25, 60),
    "Hyderabad": (29, 55),
    "Ahmedabad": (32, 45),
    "Jaipur": (31, 40),
    "Lucknow": (30, 50)
}

months = pd.date_range(start="2025-01-01", periods=12, freq="MS")

rows = []

for city, (base_temp, base_humidity) in cities.items():
    for date in months:
        month = date.month

        if month in [3, 4, 5]:
            temp_effect = 6
            humidity_effect = -8
        elif month in [6, 7, 8, 9]:
            temp_effect = -2
            humidity_effect = 15
        elif month in [12, 1, 2]:
            temp_effect = -6
            humidity_effect = 5
        else:
            temp_effect = 0
            humidity_effect = 0

        rows.append({
            "city": city,
            "date": date.strftime("%Y-%m-%d"),
            "temperature": round(base_temp + temp_effect + random.uniform(-2, 2), 1),
            "humidity": max(10, min(95, base_humidity + humidity_effect + random.randint(-8, 8)))
        })

df = pd.DataFrame(rows)
df.to_csv("data/raw/weather_data.csv", index=False)

print("Monthly weather data saved!")
print("Total Rows:", len(df))
print(df.head())
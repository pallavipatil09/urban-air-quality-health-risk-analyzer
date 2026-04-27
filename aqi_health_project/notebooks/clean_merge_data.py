import pandas as pd

# Load files
aqi = pd.read_csv("data/raw/aqi_data.csv")
weather = pd.read_csv("data/raw/weather_data.csv")
hospital = pd.read_csv("data/raw/hospital_data.csv")

# Clean city names
for df in [aqi, weather, hospital]:
    df["city"] = df["city"].str.strip().str.title()

# Convert date columns
aqi["date"] = pd.to_datetime(aqi["date"])
weather["date"] = pd.to_datetime(weather["date"])
hospital["date"] = pd.to_datetime(hospital["date"])

# Merge datasets
merged = pd.merge(aqi, weather, on=["city", "date"], how="left")
merged = pd.merge(merged, hospital, on=["city", "date"], how="left")

# AQI Category
bins = [0, 50, 100, 200, 300, 500]
labels = ["Good", "Moderate", "Unhealthy", "Very Unhealthy", "Hazardous"]

merged["aqi_category"] = pd.cut(
    merged["aqi"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Month name
merged["month"] = merged["date"].dt.strftime("%B")
merged["month_number"] = merged["date"].dt.month

# Season
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Summer"
    elif month in [6, 7, 8, 9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

merged["season"] = merged["month_number"].apply(get_season)

# Health Risk Score
merged["health_risk_score"] = (
    merged["aqi"] * 0.6 +
    merged["respiratory_cases"] * 0.4
) / 100

# Remove duplicates
merged = merged.drop_duplicates()

# Save final file
merged.to_csv("data/clean/aqi_health_final.csv", index=False)

print("Final monthly merged file saved!")
print("Final Shape:", merged.shape)
print(merged.head())
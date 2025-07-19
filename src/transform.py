import pandas as pd
from .utils import log

def transform_weather_data():
    log("Transforming weather data...")
    df = pd.read_csv("data/weather.csv")

    # Example transformation: Clean column names
    df.columns = df.columns.str.lower().str.strip()

    # Optional: create a temp column for heat index or similar
    df["temp_humidity_index"] = df["temperature"] + 0.1 * df["humidity"]

    df.to_csv("data/cleaned_weather.csv", index=False)
    log("Cleaned data saved to data/cleaned_weather.csv")

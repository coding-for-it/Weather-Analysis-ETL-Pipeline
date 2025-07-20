import requests
import pandas as pd
import os
from src.config import OPENWEATHER_API_KEY
from src.utils import log
from datetime import datetime

def fetch_weather_data(city, country, state):  # Added 'state' parameter
    log(f"Fetching weather data for {city}, {country}")
    
    # Check if API key is present
    if not OPENWEATHER_API_KEY:
        log("OPENWEATHER_API_KEY is missing or not set.")
        return None

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city},{country}&appid={OPENWEATHER_API_KEY}&units=metric"
    )
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "state": state,  # Added state here
                "city": city,
                "country": country,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "weather": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"],
                "datetime": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        else:
            log(f"Failed to fetch data for {city}, {country}. Status Code: {response.status_code}, Response: {response.text}")
            return None
    except Exception as e:
        log(f"Exception occurred while fetching data for {city}, {country}: {str(e)}")
        return None

def save_weather_data(data_list):
    if not data_list:
        log("No data to save.")
        return
    df = pd.DataFrame(data_list)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/weather.csv", index=False)
    log("Weather data saved to data/weather.csv")

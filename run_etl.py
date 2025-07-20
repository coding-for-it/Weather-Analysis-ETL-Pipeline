from src.extract import fetch_weather_data, save_weather_data
from src.transform import transform_weather_data
from src.load import load_to_postgres
from src.utils import log

import os

def run_etl():
    log("Starting ETL Pipeline...")

    state_city_map = {
        "Delhi": {"city": "Delhi", "country": "IN"},
        "Maharashtra": {"city": "Mumbai", "country": "IN"},
        "Tamil Nadu": {"city": "Chennai", "country": "IN"},
        "Karnataka": {"city": "Bangalore", "country": "IN"},
        "West Bengal": {"city": "Kolkata", "country": "IN"},
        "Rajasthan": {"city": "Jaipur", "country": "IN"},
        "Uttar Pradesh": {"city": "Lucknow", "country": "IN"},
        "Gujarat": {"city": "Ahmedabad", "country": "IN"},
        "Bihar": {"city": "Patna", "country": "IN"},
        "Andhra Pradesh": {"city": "Vijayawada", "country": "IN"},
        "Kerala": {"city": "Thiruvananthapuram", "country": "IN"},
        "Punjab": {"city": "Amritsar", "country": "IN"},
        "Haryana": {"city": "Chandigarh", "country": "IN"},
        "Odisha": {"city": "Bhubaneswar", "country": "IN"},
        "Madhya Pradesh": {"city": "Bhopal", "country": "IN"},
        "Jharkhand": {"city": "Ranchi", "country": "IN"},
        "Assam": {"city": "Guwahati", "country": "IN"},
        "Chhattisgarh": {"city": "Raipur", "country": "IN"},
        "Uttarakhand": {"city": "Dehradun", "country": "IN"},
        "Goa": {"city": "Panaji", "country": "IN"},
        "Himachal Pradesh": {"city": "Shimla", "country": "IN"},
        "Tripura": {"city": "Agartala", "country": "IN"},
        "Manipur": {"city": "Imphal", "country": "IN"},
        "Meghalaya": {"city": "Shillong", "country": "IN"},
        "Nagaland": {"city": "Kohima", "country": "IN"},
        "Mizoram": {"city": "Aizawl", "country": "IN"},
        "Sikkim": {"city": "Gangtok", "country": "IN"},
        "Arunachal Pradesh": {"city": "Itanagar", "country": "IN"}
    }

    all_weather_data = []

    for state, loc in state_city_map.items():
        record = fetch_weather_data(loc["city"], loc["country"], state)  # Passed state to function
        if record:
            all_weather_data.append(record)
        else:
            log(f"No data fetched for {state} ({loc['city']})")

    os.makedirs("data", exist_ok=True)

    save_weather_data(all_weather_data)
    log(f"Extraction complete. Records fetched: {len(all_weather_data)}")

    if not os.path.exists("data/weather.csv"):
        log("'data/weather.csv' not found after extraction. Aborting pipeline.")
        return

    transform_weather_data()
    log("Transformation complete.")

    load_to_postgres()
    log("Loading to PostgreSQL complete.")

    log("ETL Pipeline executed successfully!")

if __name__ == "__main__":
    run_etl()

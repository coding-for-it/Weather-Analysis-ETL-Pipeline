import os
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file from the root

# API key
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# DB credentials
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Check if any values are missing
if not all([OPENWEATHER_API_KEY, DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD]):
    raise EnvironmentError("Missing credentials in .env file.")

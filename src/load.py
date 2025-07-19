import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import logging

# Load environment variables from .env
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_to_postgres():
    logging.info("Loading data to PostgreSQL...")

    # Get PostgreSQL credentials from environment variables
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    if not all([host, port, db, user, password]):
        logging.error("Database credentials not properly set in .env file.")
        return

    # Create database connection string
    DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(DATABASE_URL)

    # Load transformed CSV
    df = pd.read_csv("data/cleaned_weather.csv")

    # Write to PostgreSQL
    df.to_sql("weather_data", engine, if_exists="replace", index=False)
    logging.info("Data loaded into PostgreSQL successfully.")

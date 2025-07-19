# 🌤️ Weather Analysis ETL Pipeline

A Python-based ETL pipeline that extracts real-time weather data from the OpenWeather API for major Indian cities, transforms it, and loads it into a PostgreSQL database for analysis and Power BI visualization.

## Features
- Extracts weather metrics (temperature, humidity, wind, etc.)
- Transforms and stores clean data in CSV and PostgreSQL
- Supports visualization with Power BI
- Modular code structure (Extract, Transform, Load)

## Tech Stack
- Python, Pandas
- PostgreSQL
- OpenWeather API
- Power BI

## Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/weather-etl-pipeline.git
   cd weather-etl-pipeline

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Setup environment variables:**
   ## add your API key and DB credentials.

4. **Run the pipeline:**
   ```bash
   python run_etl.py

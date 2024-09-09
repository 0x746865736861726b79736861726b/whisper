import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TELEGRAM_BOT_API = os.getenv("TELEGRAM_API_TOKEN")
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
    BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

    INFLUXDB_URL = os.getenv("INFLUXDB_URL")
    INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
    INFLUXDB_ORG = os.getenv("INFLUXDB_ORG")
    INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET")

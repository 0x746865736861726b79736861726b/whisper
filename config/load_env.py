import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TELEGRAM_BOT_API = os.getenv("TELEGRAM_API_TOKEN")
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
    BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

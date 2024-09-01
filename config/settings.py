from config.load_env import Config


class Settings:
    def __init__(self):
        self.telegram_api_token = Config.TELEGRAM_BOT_API
        self.binance_api_key = Config.BINANCE_API_KEY
        self.binance_secret_key = Config.BINANCE_SECRET_KEY

    def get_telegram_settings(self):
        return {
            "api_token": self.telegram_api_token,
        }

    def get_binance_settings(self):
        return {
            "api_key": self.binance_api_key,
            "secret_key": self.binance_secret_key,
        }

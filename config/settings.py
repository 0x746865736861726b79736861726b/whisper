from config.load_env import Config


class Settings:
    def __init__(self):
        self.telegram_api_token = Config.TELEGRAM_BOT_API
        self.binance_api_key = Config.BINANCE_API_KEY
        self.binance_secret_key = Config.BINANCE_SECRET_KEY
        self.influxdb_url = Config.INFLUXDB_URL
        self.influxdb_token = Config.INFLUXDB_TOKEN
        self.influxdb_org = Config.INFLUXDB_ORG
        self.influxdb_bucket = Config.INFLUXDB_BUCKET

    def get_telegram_settings(self):
        return {
            "api_token": self.telegram_api_token,
        }

    def get_binance_settings(self):
        return {
            "api_key": self.binance_api_key,
            "secret_key": self.binance_secret_key,
        }

    def get_influxdb_settings(self):
        return {
            "url": self.influxdb_url,
            "token": self.influxdb_token,
            "org": self.influxdb_org,
            "bucket": self.influxdb_bucket,
        }

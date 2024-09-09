from datetime import datetime

from loguru import logger
from influxdb_client import InfluxDBClient, Point, WritePrecision

from config.settings import Settings


class InfluxHandler:
    def __init__(self):
        settings = Settings().get_influxdb_settings()
        self.client = InfluxDBClient(
            url=settings["url"],
            token=settings["token"],
            org=settings["org"],
        )
        self.bucket = settings["bucket"]
        self.write_api = self.client.write_api()

    def save_data(self, symbol, price, sma):
        point = (
            Point(symbol)
            .field("price", price)
            .field("sma", sma if sma is not None else 0.0)
            .time(datetime.now(), WritePrecision.NS)
        )

        self.write_api.write(bucket=self.bucket, org=self.client.org, record=point)
        logger.debug(f"Saved data to InfluxDB: {symbol}, Price: {price}, SMA: {sma}")

    def close(self):
        self.write_api.__del__()
        self.client.__del__()

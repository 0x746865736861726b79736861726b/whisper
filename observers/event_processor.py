from collections import deque
from datetime import datetime

from loguru import logger

from observers.base_observer import Observer
from observers.handlers.influx import InfluxHandler
from observers.indicators.sma_indecator import SMAIndicator


class EventProcessor(Observer):
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id
        self.indicators = []
        self.db_handler = InfluxHandler()

    async def register_indicator(self, indicator):
        self.indicators.append(indicator)

    async def update(self, symbol, price):
        for indicator in self.indicators:
            await indicator.update(symbol, price)

        await self.process_event(symbol, float(price))

    async def process_event(self, symbol, price):
        sma_value = None
        for indicator in self.indicators:
            if isinstance(indicator, SMAIndicator) and indicator.is_ready():
                sma_value = indicator.get_value()
                break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if sma_value is not None:
            log_message = (
                f"{symbol.upper()} price is {price}. SMA {sma_value}; {timestamp}"
            )
            logger.info(log_message)
            await self.bot.send_message(self.chat_id, log_message)
        else:
            logger.debug(f"{symbol.upper()} price is {price}. SMA is not ready yet.")

        await self.db_handler.save_data(symbol, price, sma_value)

    async def close(self):
        self.db_handler.close()

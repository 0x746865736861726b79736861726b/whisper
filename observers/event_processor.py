from collections import deque
from datetime import datetime

from loguru import logger

from observers.base_observer import Observer


class EventProcessor(Observer):
    def __init__(self, bot, chat_id, sma_period=5):
        self.bot = bot
        self.chat_id = chat_id
        self.price_history = deque(maxlen=sma_period)
        self.sma_period = sma_period

    async def update(self, symbol, price):
        await self.process_event(symbol, float(price))

    async def process_event(self, symbol, price):
        self.price_history.append(price)
        sma = self.calculate_sma()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"{symbol.upper()} price is {price}. SMA {sma}; {timestamp}"
        logger.info(log_message)
        await self.bot.send_message(self.chat_id, log_message)

        await self.save_to_db(symbol, price, sma)

    def calculate_sma(self):
        return sum(self.price_history) / self.sma_period

    async def save_to_db(self, symbol, price, sma):
        log_message = f"Saving data to DB: {symbol}, Price: {price}, SMA: {sma}"
        logger.info(log_message)

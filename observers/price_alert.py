from loguru import logger

from observers.base_observer import Observer


class PriceAlert(Observer):
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id

    async def update(self, symbol, price):
        pass

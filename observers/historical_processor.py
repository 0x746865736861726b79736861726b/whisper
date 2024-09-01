from observers.base_observer import Observer
from exchange.api.api_handler import BinanceApiHandler


class InitialCandlesObserver(Observer):
    def __init__(self, bot, chat_id, symbol, period, interval, event_processor):
        self.bot = bot
        self.chat_id = chat_id
        self.symbol = symbol
        self.period = period
        self.interval = interval
        self.event_processor = event_processor

    async def update(self):
        api_handler = BinanceApiHandler()
        candles = await api_handler.get_initial_candles(
            self.symbol, self.period, self.interval
        )

        for candle in candles:
            await self.event_processor.update(self.symbol, candle)

        return candles

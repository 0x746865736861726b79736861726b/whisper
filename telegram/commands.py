from aiogram import types

from observers.price_alert import PriceAlert
from observers.event_processor import EventProcessor
from exchange.websocket_factory import WebsocketFactory
from observers.historical_processor import InitialCandlesObserver


class CommandHandler:
    def __init__(self, bot):
        self.bot = bot
        self.websocket_factory = WebsocketFactory()
        self.connector = None

    async def handle_sma_command(self, message: types.Message):
        try:
            _, exchange_name, symbol, period, interval = message.text.split()
            period = int(period)
            if period < 1:
                raise ValueError("Period must be greater than 0.")

            chat_id = message.chat.id
            await self.bot.send_message(
                chat_id,
                f"Opening WebSocket for {symbol.upper()} on {exchange_name} with SMA period {period} and interval {interval}...",
            )

            event_processor = EventProcessor(self.bot, chat_id, sma_period=period)

            # Створюємо об'єкт InitialCandlesObserver
            initial_candles_observer = InitialCandlesObserver(
                self.bot, chat_id, symbol, period, interval, event_processor
            )

            # Отримуємо початкові свічки
            await initial_candles_observer.update()

            price_alert = PriceAlert(self.bot, chat_id)

            self.connector = self.websocket_factory.create_websocket(
                exchange_name, symbol, interval
            )
            self.connector.register_observer(event_processor)
            self.connector.register_observer(price_alert)

            await self.connector.run()
        except Exception as e:
            await self.bot.send_message(message.chat.id, f"Error: {str(e)}")

    async def handle_stop_command(self, message: types.Message):
        if self.connector:
            await self.connector.stop()
            await self.bot.send_message(
                message.chat.id, "Stopped the WebSocket connection."
            )
            self.connector = None
        else:
            await self.bot.send_message(
                message.chat.id, "No active WebSocket connection found."
            )

from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from config.settings import Settings
from telegram.commands import CommandHandler


class TelegramBot:
    def __init__(self):
        settings = Settings().get_telegram_settings()
        self.bot = Bot(token=settings["api_token"])
        self.dispatcher = Dispatcher(storage=MemoryStorage())
        self.command_handler = CommandHandler(self.bot)

    def register_handlers(self):
        self.dispatcher.message.register(
            self.send_welcome, Command(commands=["start", "help"])
        )
        self.dispatcher.message.register(self.handle_sma, Command(commands=["sma"]))
        self.dispatcher.message.register(self.handle_stop, Command(commands=["stop"]))

    async def send_welcome(self, message: Message):
        await message.reply(
            "Welcome! Use /sma <symbol> <period> <interval> to get SMA."
        )

    async def handle_sma(self, message: Message):
        await self.command_handler.handle_sma_command(message)

    async def handle_stop(self, message: Message):
        await self.command_handler.handle_stop_command(message)

    async def start_polling(self):
        self.register_handlers()
        await self.dispatcher.start_polling(self.bot)

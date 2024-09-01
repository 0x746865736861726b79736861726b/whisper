import asyncio
from telegram.bot import TelegramBot


async def main():
    bot = TelegramBot()
    await bot.start_polling()


if __name__ == "__main__":
    asyncio.run(main())

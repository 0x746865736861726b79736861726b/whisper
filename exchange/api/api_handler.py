import json

import aiohttp


class BinanceApiHandler:
    def __init__(self):
        self.base_url = "https://fapi.binance.com/fapi/v1"

    async def get_initial_candles(self, symbol, period, interval):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/klines?symbol={symbol}&interval={interval}&limit={period - 1}"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return [float(candle[4]) for candle in data]
                else:
                    raise Exception("Failed to fetch initial candles.")

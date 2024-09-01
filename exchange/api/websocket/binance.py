import json
import asyncio
import websockets

from loguru import logger

from exchange.interfaces.subject import WebsocketInterface


class BinanceWebsocket(WebsocketInterface):
    def __init__(self, symbols, interval):
        self.base_url = "wss://fstream.binance.com/ws"
        self.symbols = symbols
        self.interval = interval
        self.observers = []
        self.websocket = None
        self.is_runnig = False

    async def connect(self):
        stream = f"{self.symbols.lower()}@kline_{self.interval}"
        url = f"{self.base_url}/{stream}"
        logger.debug(f"Connecting to {url}")
        async with websockets.connect(url) as websocket:
            self.websocket = websocket
            self.is_running = True
            logger.info(f"Connected to {url}")
            await self.listen(websocket)

    async def listen(self, websocket):
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                kline = data["k"]
                if kline["x"]:
                    price = kline["c"]
                    self.notify_observers(self.symbols, price)
            except websockets.ConnectionClosed:
                logger.error(f"Connection closed for {self.symbols}")
                break
            except Exception as e:
                logger.error(f"Error for {self.symbols}: {e}")

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, symbol, price):
        for observer in self.observers:
            asyncio.create_task(observer.update(symbol, price))

    async def run(self):
        await self.connect()

    async def stop(self):
        if self.is_running:
            self.is_runnig = False
            if self.websocket:
                await self.websocket.close()
            logger.debug(f"Stopped the WebSocket connection for {self.symbols}.")

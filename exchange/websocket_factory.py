from exchange.websocket.binance import BinanceWebsocket


class WebsocketFactory:
    def __init__(self):
        self.websockets = {}

    def create_websocket(self, exchange_name, symbols, interval):
        if exchange_name.lower() == "binance":
            websocket = BinanceWebsocket(symbols, interval)
            self.websockets[exchange_name] = websocket
            return websocket
        raise ValueError(f"No WebSocket implementation for {exchange_name}")

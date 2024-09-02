from collections import deque
from observers.indicators.base_indecator import BaseIndicator


class SMAIndicator(BaseIndicator):
    def __init__(self, period):
        self.period = period
        self.price_history = deque(maxlen=period)
        self.previous_price = None

    async def update(self, symbol, price):
        price = float(price)
        self.price_history.append(price)

        cross_message = self.check_sma_cross(price)
        if cross_message:
            return cross_message

        self.previous_price = price

    def is_ready(self):
        return len(self.price_history) == self.period

    def get_value(self):
        if not self.is_ready():
            return None
        return sum(self.price_history) / self.period

    def check_sma_cross(self, current_price):
        sma_value = self.get_value()
        if sma_value is None:
            return None

        if self.previous_price is not None:
            if self.previous_price < sma_value <= current_price:
                return f"Open price is below SMA. Current price: {current_price}, SMA: {sma_value}"
            elif self.previous_price > sma_value >= current_price:
                return f"Close price is above SMA. Current price: {current_price}, SMA: {sma_value}"

        return None

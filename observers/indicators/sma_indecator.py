from collections import deque

from observers.indicators.base_indecator import BaseIndicator


class SMAIndicator(BaseIndicator):
    def __init__(self, period):
        self.period = period
        self.price_history = deque(maxlen=period)

    async def update(self, symbol, price):
        self.price_history.append(float(price))

    def is_ready(self):
        return len(self.price_history) == self.period

    def get_value(self):
        if not self.is_ready():
            return None
        return sum(self.price_history) / self.period

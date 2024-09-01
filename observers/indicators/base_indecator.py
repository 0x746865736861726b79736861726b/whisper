from abc import ABC, abstractmethod


class BaseIndicator:
    async def update(self, symbol, price):
        raise NotImplementedError

    def is_ready(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError

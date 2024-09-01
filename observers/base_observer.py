from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    async def update(self, symbol, price):
        pass

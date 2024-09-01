from abc import ABC, abstractmethod


class WebsocketInterface(ABC):
    @abstractmethod
    async def run(self):
        pass

    @abstractmethod
    async def stop(self):
        pass

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

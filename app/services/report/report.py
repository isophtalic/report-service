from abc import ABC, abstractmethod # Abstract Base Classes

class Report(ABC):
    @abstractmethod
    def process(self, data: dict) -> dict:
        pass
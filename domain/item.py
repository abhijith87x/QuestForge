from abc import ABC, abstractmethod

class item(ABC):
    @abstractmethod
    def apply(self, character) -> str:
        pass
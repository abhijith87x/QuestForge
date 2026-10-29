from abc import ABC, abstractmethod

class Usable(ABC):
    @abstractmethod
    def apply(self, character) -> str:
        """Apply a consumable item's effect."""
        pass
    
class Equippable(ABC):
    @abstractmethod
    def equip(self, character) -> str:
        """Equip an item for persistent stat changes."""
        pass
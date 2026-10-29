from abc import ABC, abstractmethod
from domain.inventory import Inventory
from domain.exceptions import DeadCharacterError
from patterns.observer import GameEvent, EventBus

class Character(ABC):
    def __init__(self, name: str, health: int, attack_power: int, event_bus: EventBus | None = None):
        self.name = name
        self._health = health
        self.__max_health = health
        self.attack_power = attack_power
        self.inventory = Inventory()
        self._defense = 0
        self.event_bus = event_bus
        
    @property
    def health(self) -> int:
        return self._health
    
    @property
    def is_alive(self) -> bool:
        return self._health > 0
    
    @property
    def defense(self) -> int:
        return self._defense

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
        was_alive = self._health > 0
        actual_damage = max(amount - self._defense, 0)
        self._health = max(self._health - actual_damage, 0)
        
        if was_alive and self.health == 0 and self.event_bus is not None:
            print(f"DEBUG: {self.name} was defeated!")
            self.event_bus.publish(
                GameEvent("ENEMY_DEFEATED", {"enemy": self.name})
            )
            
        
    def heal(self, amount: int) -> None:
        self._health = min(self.__max_health, self._health + amount)
            
        

    def describe(self) -> str:
        return f"{self.name} has {self._health} HP, {self.attack_power} ATK"

    def attack(self, target: "Character") -> None:
        if not self.is_alive:
            raise DeadCharacterError(f"{self.name} is dead and cannot act")
        target.take_damage(self.attack_power)
        return f"{self.name} attacks {target.name} for {self.attack_power} damage!"
        
    @abstractmethod
    def special_ability(self, target: "Character") -> None:
        raise NotImplementedError("Subclasses must implement this method.")
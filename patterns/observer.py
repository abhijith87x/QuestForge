from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class GameEvent:
    type:str
    payload: dict
    
class Observer(ABC):
    @abstractmethod
    def on_event(self, event: GameEvent) -> None: ...
    
class EventBus:
    def __init__(self):
        self._observers:list[Observer] = []
        
    def subscribe(self,observer:Observer) -> None:
        self._observers.append(observer)
        
    def publish(self, event:GameEvent) -> None:
        for obs in self._observers:
            obs.on_event(event)
            
class CombatLogger(Observer):
    def on_event(self, event:GameEvent) -> None:
        print(f"[LOG] {event.type}: {event.payload}")
        
class AchievementTracker(Observer):
    def __init__(self):
        self.unlocked:set[str] = set()
        
    def on_event(self, event:GameEvent) -> None: 
        if event.type == "ENEMY_DEFEATED" and "First Blood" not in self.unlocked:
            self.unlocked.add("First Blood")
            print("🏆 Achievement unlocked: First Blood!")

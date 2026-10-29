from abc import ABC, abstractmethod
import random

class AIStrategy(ABC):
    @abstractmethod
    def choose_target(self,enemies:list):
        ...
    
class AggressiveAI(AIStrategy):
     def choose_target(self, enemies: list):
        # Returns the character with the lowest health
        return min(enemies, key=lambda c: c.health)

    
class RandomAI(AIStrategy):
    def choose_target(self, enemies: list):
        # Returns a random character
        return random.choice(enemies)
    
class DefensiveAI(AIStrategy):
    def choose_action(self, allies: list, enemies: list):
        low_health_allies = [
            ally for ally in allies
            if ally.health / ally.max_health < 0.30
        ]

        if low_health_allies:
            target = min(
                low_health_allies,
                key=lambda ally: ally.health / ally.max_health
            )
            return "heal", target

        target = min(enemies, key=lambda enemy: enemy.health)
        return "attack", target
    
    
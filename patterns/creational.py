from domain.character import Character
from domain.classes import Warrior, Mage, Rogue, Cleric
from domain.exceptions import InvalidActionError

class CharacterFactory:
    @staticmethod
    def create(class_type:str, name:str) -> Character:
        class_type = class_type.lower()
        if class_type == "warrior":
            return Warrior(name)
        elif class_type == "mage":
            return Mage(name)
        elif class_type == "rogue":
            return Rogue(name)
        elif class_type == "cleric":
            return Cleric(name)
        else:
            raise InvalidActionError(f"Unknown class type: {class_type}")
        
class EnemyBuilder:
    def __init__(self,name:str):
        self._enemy = Warrior(name)
        
    def with_health(self, health:int) -> 'EnemyBuilder':
        self._enemy._health = health
        return self
    
    def with_attack(self, attack:int) -> 'EnemyBuilder':
        self._enemy.attack_power = attack
        return self
    
    def with_loot(self, item) -> "EnemyBuilder":
        self._enemy.inventory.add(item)
        return self
    
    def build(self) -> Character:
        return self._enemy
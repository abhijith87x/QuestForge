from domain.character import Character

class CharacterBuff(Character):
    def __init__(self, wrapped:Character):
        self._wrapped = wrapped
        
    def __getattr__(self, name):
        return getattr(self._wrapped, name)
    
    @property
    def attack_power(self):
        return self._wrapped.attack_power
    
    def special_ability(self, target):
        return self._wrapped.special_ability(target)

class RageBuff(CharacterBuff):
    @property
    def attack_power(self):
        return int(self._wrapped.attack_power * 1.5)
    
    def  __repr__(self):
        return f"Raging({self._wrapped.name})"
    
class PoisonDebuff(CharacterBuff):
    def __init__(self, wrapped:Character, damage_per_turn:int = 5):
        super().__init__(wrapped)
        self.damage_per_turn = damage_per_turn
        
    def tick(self) -> str:
        self._wrapped.take_damage(self.damage_per_turn)
        return f"{self._wrapped.name} takes {self.damage_per_turn}poison damage!"

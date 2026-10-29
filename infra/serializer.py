from domain.classes import Warrior, Mage, Rogue

_CLASS_MAP = {"Warrior":Warrior, "Mage":Mage, "Rogue": Rogue}

def character_to_dict(character) -> dict:
    return {
        "type":type(character).__name__,
        "name":character.name,
        "health":character.health,
        "attack_power":character.attack_power,
    }
    
def character_from_dict(data:dict):
    cls = _CLASS_MAP[data["type"]]
    character = cls(data["name"])
    character._health = data["health"]
    character.attack_power = data["attack_power"]
    return character
class Character:
    def __init__(self, name: str, health: int, attack_power: int, heal: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.heal = heal

    def describe(self) -> str:
        return f"{self.name} has {self.health} HP, {self.attack_power} ATK, and can heal for {self.heal} HP"

    def attack(self, target: "Character") -> None:
        target.health -= self.attack_power
        target.health += target.heal 
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
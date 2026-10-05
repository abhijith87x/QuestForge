from domain.character import Character

def run_special_round(attacker: Character, defender: Character) -> None:
    attacker.special_ability(defender)
    
from domain.classes import Warrior, Mage, Rogue, Cleric
from domain.items import HealthPotion, Weapon, Armor
from domain.exceptions import QuestForgeError

if __name__ == "__main__":

#   warrior = Warrior("abhi")
# Create items
# potion1 = HealthPotion()
# potion2 = HealthPotion()
# weapon = Weapon("Iron Sword", 10)
# armor = Armor("Steel Armor", 5)

# # Add them to Warrior's inventory
# warrior.inventory.add(potion1)
# warrior.inventory.add(potion2)
# warrior.inventory.add(weapon)
# warrior.inventory.add(armor)

# # See inventory
# print(warrior.inventory.list_items())

# warrior.attack(warrior)
# print(warrior.describe())
#   warrior.inventory.use(0, warrior)  # Use first potion
# print(warrior.describe())

    mage =  Mage("Sylla")
    warrior = Warrior("Bram")

    try:
        warrior.inventory.use(0, warrior) 
        mage.special_ability(warrior)
        mage.special_ability(warrior)
        mage.special_ability(warrior)
        
    except QuestForgeError as e:
        print(f"Action failed: {e}")
    
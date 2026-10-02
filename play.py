from domain.classes import Warrior, Mage, Rogue, Cleric

if __name__ == "__main__":
    # Create characters
    warrior = Warrior("Aragorn")
    mage = Mage("Gandalf")
    rogue = Rogue("Legolas")
    cleric = Cleric("Elrond")

    # Display initial states
    print(warrior.describe())
    print(mage.describe())
    print(rogue.describe())
    print(cleric.describe())

    # Simulate a battle
    warrior.attack(mage)
    mage.special_ability(warrior)
    rogue.special_ability(mage)
    cleric.special_ability(warrior)

    # Display final states
    print(warrior.describe())
    print(mage.describe())
    print(rogue.describe())
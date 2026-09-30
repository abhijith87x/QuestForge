from domain.character import Character

if __name__ == "__main__":
    hero = Character("Aria", 100, 15, 5)
    goblin = Character("Goblin", 30, 5, 5)
    ironman = Character("ironman", 150, 100, 50)
    thor = Character("thor", 200, 150, 150)
    
    print(hero.describe())
    print(goblin.describe())
    print(ironman.describe())
    
    hero.attack(goblin)
    print(goblin.describe())
    
    thor.attack(ironman)
    print(ironman.describe())
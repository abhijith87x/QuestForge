from patterns.facade import CharacterFactory
from patterns.strategy import AggressiveAI
from domain.classes import Warrior
from patterns.decorators import PoisonDebuff
from patterns.command import AttackCommand, CommandHistory
from domain.classes import Warrior

def test_factory_creates_correct_type():
    unit = CharacterFactory.create("mage", "test")
    assert type(unit).__name__ == "Mage"
    
def test_aggressive_ai_targets_lowest_health():
    weak = Warrior('weak')
    weak.take_damage(100)
    strong = Warrior("strong")
    target = AggressiveAI().choose_target([weak, strong])
    assert target is weak
    
def test_poison_debuff_reduces_hp():
    hero = Warrior('test')
    poison = PoisonDebuff(hero)
    poison.tick()
    assert hero.health == 115
    
def test_undo_last_attack_restores_hp():
    attacker = Warrior("Hero")
    target = Warrior("Enemy")
    
    history = CommandHistory()
    attack = AttackCommand(attacker, target)
    
    initail_health = target.health
   
    history.run(attack)
    assert target.health == initail_health - attacker.attack_power

    # Undo the attack
    history.undo_last()

    # Check that HP is restored
    assert target.health == initail_health
    
   
    
    
    
from domain.classes import Warrior

def test_take_damage_clamps_at_zero():
    hero = Warrior("Test")
    hero.take_damage(9999)
    assert hero.health == 0
    assert hero.is_alive is False


def test_heal_does_not_exceed_max_health():
    hero = Warrior("test")
    hero.take_damage(50)
    hero.heal(9999)
    assert hero.health == 120
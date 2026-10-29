# QuestForge — SOLID Refactor Notes

## S — Single Responsibility Principle

### Before

`Character` was responsible for both performing combat actions and printing combat messages.

```python
def attack(self, target):
    target.take_damage(self.attack_power)
    print(f"{self.name} attacks {target.name}!")
```

### After

`Character` performs the action and returns a message. `play.py` is responsible for displaying it.

```python
def attack(self, target):
    target.take_damage(self.attack_power)
    return f"{self.name} attacks {target.name}!"
```

This gives `Character` one main responsibility instead of making it responsible for console output too.

---

## O — Open/Closed Principle

### Before

A system could require `if/elif` checks for every character type.

```python
if unit_type == "warrior":
    ...
elif unit_type == "mage":
    ...
```

### After

Each character type is its own class.

```python
class Warrior(Character):
    ...

class Mage(Character):
    ...
```

New character types can be added without modifying the existing character classes.

---

## L — Liskov Substitution Principle

### Before

A subclass should not change the expected behavior of the `Character` class.

### After

All concrete character classes inherit from `Character` and follow the same basic behavior for methods such as:

```python
take_damage()
heal()
attack()
```

A `Warrior`, `Mage`, or other `Character` can be used wherever a `Character` is expected.

---

## I — Interface Segregation Principle

### Before

There was one large `Item` interface:

```python
class Item(ABC):
    @abstractmethod
    def apply(self, character):
        pass
```

As more item behaviors were added, different items could be forced to implement methods they did not need.

### After

The item interface was split into smaller interfaces:

```python
class Usable(ABC):
    @abstractmethod
    def apply(self, character):
        pass


class Equippable(ABC):
    @abstractmethod
    def equip(self, character):
        pass
```

Now a `HealthPotion` implements `Usable`, while a `Weapon` implements `Equippable`.

---

## D — Dependency Inversion Principle

### Before

A high-level class could directly create a concrete dependency.

```python
self.saver = FileSaver()
```

This tightly couples the class to `FileSaver`.

### After

The high-level code should depend on an abstraction and receive the concrete implementation from outside.

```python
class SaveAdapter(ABC):
    @abstractmethod
    def save(self, character):
        pass
```

The concrete saver can then be supplied externally.

This makes the code easier to replace and test.

---

## Summary

The Level 8 refactor improves QuestForge by applying the five SOLID principles:

* **S — SRP:** Separate combat logic from console output.
* **O — OCP:** Add new character types without modifying existing code.
* **L — LSP:** Subclasses honor the behavior expected from `Character`.
* **I — ISP:** Split large interfaces into smaller, focused interfaces.
* **D — DIP:** Depend on abstractions instead of concrete implementations.

These changes make the code easier to maintain, extend, test, and prepare for future design patterns.

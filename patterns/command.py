from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...

class AttackCommand(Command):
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target
        self.damage_dealt = 0
        
    def execute(self) -> None:
        self.damage_dealt = self.attacker.attack_power
        self.target.take_damage(self.damage_dealt)
        print(
        f"{self.attacker.name} attacks {self.target.name} "
        f"for {self.damage_dealt} damage!"
    )
        
    def undo(self) -> None:
        self.target.heal(self.damage_dealt)
        
class CommandHistory:
    def __init__(self):
        self._history: list[Command] = []


    def run(self, command: Command) -> None:
        command.execute()
        self._history.append(command)


    def undo_last(self) -> None:
        if self._history:
            self._history.pop().undo()

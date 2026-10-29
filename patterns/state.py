from enum import Enum, auto

class BattleState(Enum):
    IDLE = auto()
    PLAYER_TURN = auto()
    ENEMY_TURN = auto()
    RESOLUTION = auto()
    VICTORY = auto()
    DEFEAT = auto()
    
class BattleStateMachine:
    _TRANSITIONS = {
        BattleState.IDLE: {BattleState.PLAYER_TURN},
        BattleState.PLAYER_TURN: {BattleState.ENEMY_TURN},
        BattleState.ENEMY_TURN: {BattleState.RESOLUTION},
        BattleState.RESOLUTION: {BattleState.PLAYER_TURN, BattleState.VICTORY, BattleState.DEFEAT},
        BattleState.VICTORY: set(),
        BattleState.DEFEAT: set(),
    }
    
    def __init__(self):
        self.state = BattleState.IDLE
    
    def transition(self, new_state: BattleState) -> None:
        if new_state not in self._TRANSITIONS[self.state]:
            raise ValueError(f"Illegal transition: {self.state} -> {new_state}")
        self.state = new_state
class QuestForgeError(Exception):
    pass

class DeadCharacterError(QuestForgeError):
    pass

class InsufficientManaError(QuestForgeError):
    pass


class InvalidActionError(QuestForgeError):
    pass


class InventoryEmptyError(QuestForgeError):
    pass
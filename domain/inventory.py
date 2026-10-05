from domain.exceptions import QuestForgeError

class Inventory:
    def __init__(self):
        self.items = []
        
    def add(self, item) -> None:
        self.items.append(item)
        
    def use(self, index: int, target) -> str:
        if index < 0 or index >= len(self.items):
            raise QuestForgeError("Invalid item index.")
        item = self.items.pop(index)
        return item.apply(target)
    
    def list_items(self) -> str:
        return [type(i).__name__ for i in self.items]
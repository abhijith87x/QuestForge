from patterns.singleton import GameManager
from patterns.creational import CharacterFactory
from domain.exceptions import QuestForgeError
from infra.serializer import character_from_dict, character_to_dict

class QuestForgeAPI:
    def __init__(self, save_adapter):
        self.manager = GameManager() 
        self.save_adapter = save_adapter
        
    def new_game(self, class_names_and_names:list[tuple[str,str]])->None:
        party = [CharacterFactory.create(cls, name) for cls, name in class_names_and_names]
        self.manager.start_new_session(party)
        
    def save(self) -> None:
        # Hides the format of the save data and the adapter being used
        data = {
            "turn_count": self.manager.turn_count,
            "party": [character_to_dict(c) for c in self.manager.party]
        }
        self.save_adapter.save(data)
        
    def load(self) -> None:
        data = self.save_adapter.load()
        self.manager.turn_count = data["turn_count"]
        
        # Reconstruct the live objects from the dictionary data
        self.manager.party = [character_from_dict(d) for d in data["party"]]
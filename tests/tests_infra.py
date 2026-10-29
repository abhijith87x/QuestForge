from infra.save_adapter import inMemoryAdapter
from patterns.facade import QuestForgeAPI

def test_save_and_load_round_trip():
    api = QuestForgeAPI(inMemoryAdapter())
    api.new_game([("Warrior", "Hero")])
    api.save
    
    api.manager.party = []
    api.load
    
    assert api.manager.party[0].name == 'Hero'
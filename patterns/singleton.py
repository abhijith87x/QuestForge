class GameManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialized = False
        return cls._instance
    
    def __init__(self):
        if  self.initialized:
            return 
        
        self.party:list = []
        self.turn_count:int = 0
        self.difficulty:str = 'normal'
        self.initialized = True
        
    def start_new_session(self, party: list) -> None:
        self.party = party
        self.turn_count = 0


    def next_turn(self) -> int:
        self.turn_count += 1
        return self.turn_count
        
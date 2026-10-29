from abc import ABC, abstractmethod
import json

class SaveAdaptor(ABC):
    @abstractmethod
    def save(self, data:dict) -> None:...
    @abstractmethod
    def load(self)-> dict:
        pass
    
class JsonFileAdapter(SaveAdaptor):
    def __init__(self,path:str='save.json'):
        self.path = path
        
    def save(self,data:dict)-> None:
        with open(self.path, "w") as f:
            json.dump(data, f,indent=2)
            
    def load(self)->dict:
        with open(self.path) as f:
            return json.load(f)
        
class inMemoryAdapter(SaveAdaptor):
    def __init__(self):
        self._data: dict = {}
        
    def save(self,data:dict)->None:
        self._data = data
        
    def load(self)->dict:
        return self._data
        
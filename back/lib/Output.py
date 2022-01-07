from Settings import Settings
import json
from json import  JSONEncoder


class Output():
    def __init__(self, res, history, settings: Settings, graph:dict, tree:dict) -> None:
        self.result = res
        self.history = history
        self.settings = settings
        self.graph = graph
        self.tree = tree
        self.nbMoves = len(history) - 1
    
    def toJson(self):
        self.result = json.dumps(self.result.tolist())
        self.history = json.dumps(self.history.tolist())

class OutputEncoder(JSONEncoder):
    def default(self, o):
            return o.__dict__
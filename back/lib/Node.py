import numpy as np

class Node():
    def __init__(self) -> None:
        pass

    def npToString(self, state: np.array):
        return ''.join(str(m) for m in state.ravel())

    def findIdNodeInTree(self, json, id: str):
        obj = None
        if json["id"] == id: return json

        for child in json["children"]:
            obj = self.findIdNodeInTree(child, id)
            if obj is not(None):
                if obj["id"] == id: return obj
        return obj

    def addTreeChildren(self, parent, child: str):
        if parent == None: print("[Error] parent node is None")
        parent['children'].append({"id": child, "children": []})
    
    def addNodeGraph(self, graph:dict, id: str):
        graph["nodes"].append({"id": id})
    
    def addLinkGraph(self, graph:dict, source: str, target: str):
        graph["links"].append({"source": source, "target": target})

    def graphHandle(self, graph, source, target):
        alreadyExist = False

        for node in graph["nodes"]:
            if node["id"] == target: alreadyExist = True
        if not(alreadyExist): self.addNodeGraph(graph, target)
        self.addLinkGraph(graph, source, target)

    
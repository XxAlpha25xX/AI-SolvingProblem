
import numpy as np
import sys
import os
import json
#print(sys.path)

LIB_PATH = os.path.abspath(os.getcwd()) + '/../lib/'
sys.path.append(LIB_PATH)
from Node import Node
from Puzzle import Puzzle
from Error import ErrorCodex as Error
from Settings import Settings
from Output import Output


class BreadthFirstSearch():
    def __init__(self) -> None:
        self._puzzle = Puzzle()
        self._err = Error()
        self._node = Node()
        self.expectedShape = np.array([(3, 3), (5, 5)])

    def initVar(self, state: np.array):
        self.size = state.shape[0]
        self.shape = (self.size, self.size)
        self.arrayShape = (-1, self.size, self.size)
        self.len = self.size * self.size

    def enginePuzzle(self, state: np.array, settings: Settings) -> np.array:
        i = 0
        res = None
        self._visitedNode = np.array([])
        self._queue = np.array([])
        tree = {"id": self._node.npToString(state), "children": []} #
        graph = {"nodes" : [], "links": []}

        self.initVar(state)
        self._goal = np.append(np.arange(1,self.len), 0).reshape(self.shape)
        self._queue = np.append(self._queue, np.copy(state)).astype(int).reshape(self.arrayShape)
        while res is None:
            res = self.visitTopQueue(tree, graph, settings)
            i += 1
            if i >= settings.maxIter: res = np.array([])
        return Output(res=res, history=self._visitedNode, settings=settings, graph=graph, tree=tree)

    def visitTopQueue(self, tree: dict, graph: dict, settings: Settings) -> None:
        try:
            if len(self._queue) == 0: self._err.BFSQueueEmpty()
            top = self._queue[0]
            if self.checkSolved(top): return top
            self._visitedNode = np.append(self._visitedNode, top).reshape(self.arrayShape) #Add the top to visited node
            self.addChildrenToQueue(top, tree, graph, settings)
            self._queue = np.delete(self._queue, 0, axis=0) # Remove the top of the queue          
            return None
        except Exception as e:
            print(e)
            return 84
    
    def addChildrenToQueue(self, state: np.array, tree: dict, graph: dict, settings: Settings):
        if self._puzzle.isGoodPuzzle(state) : self._err.IncorrectNumpyShape(state.shape, self.expectedShape)
        searchSpace = self._puzzle.createAllSwapPossibility(state, self._puzzle.getSwapPossibility(state)).reshape(self.arrayShape)
        for tmp in searchSpace:
            if not(settings.isGraph) and self._visitedNode.shape[0] > 0:
                if not(self.checkAlreadyVisitedNode(tmp)):
                    self._queue = np.append(self._queue, np.copy(tmp)).astype(int).reshape(self.arrayShape)
                    self._node.addTreeChildren(self._node.findIdNodeInTree(tree, self._node.npToString(np.copy(state))), self._node.npToString(np.copy(tmp)))
            elif settings.isGraph:
                self._queue = np.append(self._queue, np.copy(tmp)).astype(int).reshape(self.arrayShape)
                self._node.graphHandle(graph, self._node.npToString(np.copy(state)), self._node.npToString(np.copy(tmp)))

    def checkAlreadyVisitedNode(self, state) -> bool:
        for node in self._visitedNode:
            if np.array_equal(node, state): return True
        return False

    def checkSolved(self, state: np.array) -> bool:
        return np.array_equal(self._goal, state)

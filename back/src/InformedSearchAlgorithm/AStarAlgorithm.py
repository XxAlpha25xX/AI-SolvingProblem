import numpy as np
import sys
import os
import random
import json


LIB_PATH = os.path.abspath(os.getcwd()) + '/../lib/'
sys.path.append(LIB_PATH)
from Puzzle import Puzzle
from Error import ErrorCodex as Error
from Output import Output, OutputEncoder
from Settings import Settings
from Node import Node


class AStarAlgorithm():
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

    def enginePuzzle(self, state: np.array, settings: Settings) -> Output:
        res = None
        i = 0
        self._visitedNode = np.array([])
        self._queue = np.array([])
        self.initVar(state)
        self._goal = np.append(np.arange(1,self.len), 0).reshape(self.shape)
        self._queue = np.append(self._queue, np.copy(state)).astype(int).reshape(self.arrayShape)
        tree = {"id": self._node.npToString(state), "children": []}
        graph = {"nodes" : [{"id":self._node.npToString(state)}], "links": []}

        while res is None:
            res = self.visitTopQueue(tree, graph, settings)
            i += 1
            if i >= settings.maxIter: res = np.array([])
        return Output(res=res, history=self._visitedNode.astype(int).reshape(self.arrayShape), settings=settings, graph=graph, tree=tree)

    
    def visitTopQueue(self, tree: dict, graph: dict, settings: Settings) -> None:
        try:
            if len(self._queue) == 0: self._err.BFSQueueEmpty()
            top = self.pickBestQueue()
            if self.checkSolved(top): return top
            self._visitedNode = np.append(self._visitedNode, top).reshape(self.arrayShape) #Add the top to visited node
            self.addChildrenToQueue(top, tree, graph, settings)
            return None
        except Exception as e: 
            print(e)
            return 84

    def pickBestQueue(self) -> np.array:
        self._queue = self._queue.reshape(self.arrayShape)
        f = self.f()
        index = [e for e in range(0, len(f)) if f[e] == f[np.argmin(f)]]
        i = random.choice(index)
        top = np.copy(self._queue[i])
        for n in range(0, len(self._queue), 1): 
            if n != i: self._visitedNode = np.append(self._visitedNode, np.copy(self._queue[n]))
        self._queue = np.array([])
        return top

    def h(self) -> int:
        return self._puzzle.sumManhatanDistance(self._queue, self.size)

    def g(self) -> int:
        return self._puzzle.countMisplacedTile(self._queue, self.size)

    def f(self) -> int:
        h = self.h()
        g = self.g()
        f = np.add(np.array(h), np.array(g))
        return f


    def addChildrenToQueue(self, state: np.array, tree: dict, graph: dict, settings: Settings):
        if self._puzzle.isGoodPuzzle(state) : self._err.IncorrectNumpyShape(state.shape, self.expectedShape)
        moves = self._puzzle.getSwapPossibility(state)
        searchSpace = self._puzzle.createAllSwapPossibility(state, moves)
        searchSpace = searchSpace.reshape(self.arrayShape)
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
            if np.array_equal(node, state) == True: return True
        return False

    def checkSolved(self, state: np.array) -> bool:
        return np.array_equal(self._goal, state)

#print(json.dumps(out, indent=4, cls=OutputEncoder))
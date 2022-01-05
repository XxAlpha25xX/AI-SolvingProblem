import numpy as np
import sys
import os
import random

from numpy.lib.function_base import delete

LIB_PATH = os.path.abspath(os.getcwd()) + '/../lib/'
sys.path.append(LIB_PATH)
from Puzzle import Puzzle
from Error import ErrorCodex as Error

MAX_ITER = 10000

class AStarAlgorithm():
    def __init__(self) -> None:
        self._visitedNode = np.array([])
        self._queue = np.array([])
        self._puzzle = Puzzle()
        self._err = Error()
        self.expectedShape = np.array([(3, 3), (5, 5)])

    def initVar(self, iS: np.array):
        self.size = iS.shape[0]
        self.shape = (self.size, self.size)
        self.arrayShape = (-1, self.size, self.size)
        self.len = self.size * self.size

    def enginePuzzle(self, iS: np.array) -> np.array:
        i = 0
        res = None
        self.initVar(iS)
        self._goal = np.append(np.arange(1,self.len), 0).reshape(self.shape)
        self._queue = np.append(self._queue, np.copy(iS)).astype(int).reshape(self.arrayShape)

        while res is None:
            res = self.visitTopQueue()
            i += 1
            if i >= MAX_ITER: res = np.array([])
        return res, self._visitedNode

    
    def visitTopQueue(self) -> None:
        try:
            if len(self._queue) == 0: self._err.BFSQueueEmpty()
            top = self.pickBestQueue()
            if self.checkSolved(top): return top
            self._visitedNode = np.append(self._visitedNode, top).reshape(self.arrayShape) #Add the top to visited node
            self.addChildrenToQueue(top)
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
        g = [1]
        f = np.add(np.array(h), np.array(g))
        return f


    def addChildrenToQueue(self, iS: np.array):
        if self._puzzle.isGoodPuzzle(iS) : self._err.IncorrectNumpyShape(iS.shape, self.expectedShape)
        moves = self._puzzle.getSwapPossibility(iS)
        searchSpace = self._puzzle.createAllSwapPossibility(iS, moves)
        searchSpace = searchSpace.reshape(self.arrayShape)
        for tmp in searchSpace:
            if self.checkAlreadyVisitedNode(tmp) == False:
                self._queue = np.append(self._queue, np.copy(tmp)).astype(int).reshape(self.arrayShape)

    def checkAlreadyVisitedNode(self, iS) -> bool:
        for state in self._visitedNode:
            if np.array_equal(iS, state) == True: return True
        return False

    def checkSolved(self, iS: np.array) -> bool:
        return np.array_equal(self._goal, iS)

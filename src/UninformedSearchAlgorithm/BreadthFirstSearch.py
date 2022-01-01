from Node import Node
import numpy as np
import sys
import os
#print(sys.path)

LIB_PATH = os.path.abspath(os.getcwd()) + '/../lib/'
sys.path.append(LIB_PATH)
from Puzzle import Puzzle
from Error import ErrorCodex as Error

MAX_ITER = 10000000

class BreadthFirstSearch():
    def __init__(self) -> None:
        self._visitedNode = np.array([])
        self._queue = np.array([])
        self._puzzle = Puzzle()
        self._err = Error()
        self.expectedShape = np.array([(3, 3), (5, 5)])

    def engine(self, iS: np.array) -> np.array:
        i = 0
        res = None
        s = iS.shape[0]

        self._goal = np.append(np.arange(1,s * s), 0).reshape(s, s)
        self._queue = np.append(self._queue, np.copy(iS)).astype(int).reshape(-1, s, s)
        while res is None:
            res = self.visitTopQueue()
            i += 1
            if i >= MAX_ITER: res = np.array([])
        return res, self._visitedNode

    
    def visitTopQueue(self) -> None:
        try:
            if len(self._queue) == 0: self._err.BFSQueueEmpty()
            top = self._queue[0]
            if self.checkSolved(top): return top
            self._visitedNode = np.append(self._visitedNode, top).reshape(-1, 3, 3) #Add the top to visited node
            self.addChildrenToQueue(top)
            self._queue = np.delete(self._queue, 0, axis=0) # Remove the top of the queue            
            return None
        except Exception as e: 
            print(e)
            return 84
    
    def addChildrenToQueue(self, iS: np.array):
        if self._puzzle.isGoodPuzzle(iS) : self._err.IncorrectNumpyShape(iS.shape, self.expectedShape)
        moves = self._puzzle.getSwapPossibility(iS)
        searchSpace = self._puzzle.createAllSwapPossibility(iS, moves)
        searchSpace = searchSpace.reshape((-1, iS.shape[0], iS.shape[0]))
        size = iS.shape[0]
        for tmp in searchSpace:
            if self.checkAlreadyVisitedNode(tmp) == False:
                self._queue = np.append(self._queue, np.copy(tmp)).astype(int).reshape(-1, size, size)

    def checkAlreadyVisitedNode(self, iS) -> bool:
        for state in self._visitedNode:
            if np.array_equal(iS, state) == True: return True
        return False

    def checkSolved(self, iS: np.array) -> bool:
        return np.array_equal(self._goal, iS)


solvedPuzzle = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
])

badShape = np.array([
    1,2,3
])

ex8Puzzle01 = np.array([
        [4, 1, 3],
        [7, 2, 6],
        [0, 5, 8]
])

ex8Puzzle02 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
])

c = BreadthFirstSearch()

c.engine(ex8Puzzle01)

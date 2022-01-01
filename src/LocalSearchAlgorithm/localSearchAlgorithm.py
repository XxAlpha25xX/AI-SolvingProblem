import numpy as np
import sys
import os
#print(sys.path)

LIB_PATH = os.path.abspath(os.getcwd()) + '/../lib/'
print(LIB_PATH)
sys.path.append(LIB_PATH)
from numpy.core.fromnumeric import shape
from Error import ErrorCodex as Err
from Scoring import Score as Score
from Puzzle import Puzzle as Puzzle
import random

MAX_ITER = 1000

class LocalSearchAlgorithm():

    # [blank] -- Init
    def __init__(self):
        self.expectedShape = np.array([(3, 3), (5, 5)])
        self._err = Err()
        self._score = Score()
        self._puzzle = Puzzle()
    
    # [bool] -- Check if it's a 8Puzzle or 24Puzzle
    def isGoodPuzzle(self, iS: np.array) -> bool:
        return not(iS.shape == (3, 3) or iS.shape == (5, 5))
    
    # [bool] -- Check if stuck
    def isStuck(self, arr, iS: np.array) -> bool:
        if np.array_equal(iS, arr[len(arr) - 1]):
            return True
        if len(arr) >= 2 and np.array_equal(iS, arr[len(arr) - 2]):
            return True

    # [np.array] -- Try to find the local maxima
    def hillClimbing(self, iS: np.array) -> np.array:
        try:
            arr = [np.copy(iS)]
            maxima = False
            iterations = 0

            while maxima == False:
                if self.isGoodPuzzle(iS) : self._err.IncorrectNumpyShape(iS.shape, self.expectedShape)
                moves = self._puzzle.getSwapPossibility(iS)
                searchSpace = self._puzzle.createAllSwapPossibility(iS, moves)
                searchSpace = searchSpace.reshape((-1, iS.shape[0], iS.shape[0]))
                i = self.sumManhatanDistance(searchSpace)
                index = [e for e in range(0, len(i)) if i[e] == i[np.argmin(i)]]
                iS = searchSpace[random.choice(index)]
                if i[np.argmin(i)] == 0: maxima = True
                elif iterations > MAX_ITER: maxima = True
                else: arr.append(np.copy(iS))
                iterations += 1
            arr.append(np.copy(iS))
            return iS, arr
        except Exception as e: print(e)
        
    def sumManhatanDistance(self, lst: np.array):
        arr = []
        for p in lst:
            score = 0
            pc = np.copy(p)
            for i in range(1, 9, 1):
                item = self._puzzle.findTileNumber(pc, i)
                goal = (abs(((i- 1) % 3)), abs(int((i - 1) / pc.shape[0])) )
                s = self._score.manhatanDistance(item, goal)
                score += s
            arr.append(score)
        return arr

import numpy as np
import sys
import os
#print(sys.path)

LIB_PATH = os.path.abspath(os.getcwd()) + '/../lib/'
sys.path.append(LIB_PATH)
from Error import ErrorCodex as Err
from Scoring import Score as Score
from Puzzle import Puzzle as Puzzle
import random

MAX_ITER = 1000

class HillClimbing():

    # [blank] -- Init
    def __init__(self):
        self.expectedShape = np.array([(3, 3), (5, 5)])
        self._err = Err()
        self._score = Score()
        self._puzzle = Puzzle()
    
    def initVar(self, iS: np.array):
        self.size = iS.shape[0]
        self.shape = (self.size, self.size)
        self.arrayShape = (-1, self.size, self.size)
        self.len = self.size * self.size

    # [np.array] -- Try to find the local maxima
    def hillClimbing(self, iS: np.array) -> np.array:
        try:
            arr = [np.copy(iS)]
            maxima = False
            iterations = 0
            size = iS.shape[0]

            self.initVar(iS)
            while maxima == False:
                if self._puzzle.isGoodPuzzle(iS) : self._err.IncorrectNumpyShape(iS.shape, self.expectedShape)
                moves = self._puzzle.getSwapPossibility(iS)
                searchSpace = self._puzzle.createAllSwapPossibility(iS, moves)
                searchSpace = searchSpace.reshape(self.arrayShape)
                i = self._puzzle.sumManhatanDistance(searchSpace, size)
                index = [e for e in range(0, len(i)) if i[e] == i[np.argmin(i)]]
                iS = searchSpace[random.choice(index)]
                if i[np.argmin(i)] == 0: maxima = True
                elif iterations > MAX_ITER: maxima = True
                else: arr.append(np.copy(iS))
                iterations += 1
            arr.append(np.copy(iS))
            return iS, arr
        except Exception as e: print(e)

import numpy as np
from numpy.core.fromnumeric import shape
from Error import ErrorCodex as err
from Scoring import Score as score
import random

MAX_ITER = 1000

class LocalSearchAlgorithm():

    # [blank] -- Init
    def __init__(self):
        self.expectedShape = np.array([(3, 3), (5, 5)])
        self.err = err()
        self.score = score()
    
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
                if self.isGoodPuzzle(iS) : self.err.IncorrectNumpyShape(iS.shape, self.expectedShape)
                moves = self.getSwapPossibility(iS)
                searchSpace = self.createAllSwapPossibility(iS, moves)
                searchSpace = searchSpace.reshape(-1, iS.shape[0], iS.shape[0])
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
    
    #[np.array] -- Swap two case of puzzle
    def swapCasePuzzle(self, iS: np.array, pos1: tuple, pos2: tuple) -> np.array:
        try:
            tmp = iS[pos1[1]][pos1[0]]
            iS[pos1[1]][pos1[0]] = iS[pos2[1]][pos2[0]]
            iS[pos2[1]][pos2[0]] = tmp
            return iS
        except Exception as e: print(e)

    #[tuple(int, int)] -- Return position of empty space -- the empty space is a zero
    def findTileNumber(self, iS: np.array, nb: int) -> tuple[int, int]:
        try:
            x = 0;
            y = 0;
            for row in iS:
                x = 0
                for col in row:
                    if col == nb: return (x, y)
                    x += 1
                y += 1;
            self.err.NoTileNumber(nb)
        except Exception as e: print(e)
    
    # 0 -> x , 1 -> y
    # [list( tuple(int, int))] -- Check all the swap possibility
    def getSwapPossibility(self, iS: np.array) -> list:
        blank = self.findTileNumber(iS, 0)
        arr = []
        if blank[0] - 1 >= 0: arr.append((blank[0] - 1, blank[1]))
        if blank[0] + 1 < iS.shape[0]: arr.append((blank[0] + 1, blank[1]))
        if blank[1] - 1 >= 0: arr.append((blank[0], blank[1] - 1))
        if blank[1] + 1 <= iS.shape[0]: arr.append((blank[0], blank[1] + 1))
        return arr
    
    def createAllSwapPossibility(self, iS: np.array, lst: list) -> np.array:
        arr = np.array([]).astype(int)
        blank = self.findTileNumber(iS, 0)
        for elem in lst:
            iSc = np.copy(iS)
            tmp = self.swapCasePuzzle(iSc, blank, elem)
            if not(tmp is None):arr = np.append(arr, tmp)
        return arr
        
    def sumManhatanDistance(self, lst: np.array):
        arr = []
        for p in lst:
            score = 0
            pc = np.copy(p)
            for i in range(1, 9, 1):
                item = self.findTileNumber(pc, i)
                goal = (abs(((i- 1) % 3)), abs(int((i - 1) / pc.shape[0])) )
                s = self.score.manhatanDistance(item, goal)
                score += s
            arr.append(score)
        return arr


# [Start Program] -- Test
lSA = LocalSearchAlgorithm()
arr1 = np.array([1, 2, 3])
solved8Puzzle = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

ex8Puzzle = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
])

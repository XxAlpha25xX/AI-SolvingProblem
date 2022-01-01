import sys
import numpy as np
from Error import ErrorCodex as Error
from Scoring import Score as Score

class Puzzle():
    def __init__(self):
        self._err = Error()
        self._score = Score()
        pass

    #[np.array] -- Swap two case of puzzle
    def swapCasePuzzle(self, iS: np.array, pos1: tuple, pos2: tuple) -> np.array:
        try:
            tmp = iS[pos1[1]][pos1[0]]
            iS[pos1[1]][pos1[0]] = iS[pos2[1]][pos2[0]]
            iS[pos2[1]][pos2[0]] = tmp
            return iS
        except Exception as e: print(e)

    # [bool] -- Check if it's a 8Puzzle or 24Puzzle
    def isGoodPuzzle(self, iS: np.array) -> bool:
        return not(iS.shape == (3, 3) or iS.shape == (5, 5))

    # 0 -> x , 1 -> y
    # [list( tuple(int, int))] -- Check all the swap possibility
    def getSwapPossibility(self, iS: np.array) -> list:
        blank = self.findTileNumber(iS, 0)
        arr = []
        if blank[0] - 1 >= 0: arr.append((blank[0] - 1, blank[1]))
        if blank[0] + 1 < iS.shape[0]: arr.append((blank[0] + 1, blank[1]))
        if blank[1] - 1 >= 0: arr.append((blank[0], blank[1] - 1))
        if blank[1] + 1 < iS.shape[0]: arr.append((blank[0], blank[1] + 1))
        return arr

    #[np.array] - Generate all swap possibility within a puzzle
    def createAllSwapPossibility(self, iS: np.array, lst: list) -> np.array:
        arr = np.array([]).astype(int)
        blank = self.findTileNumber(iS, 0)
        for elem in lst:
            iSc = np.copy(iS)
            tmp = self.swapCasePuzzle(iSc, blank, elem)
            arr = np.append(arr, tmp)
#        arr = arr[arr != None]
        return arr

    #[tuple(int, int)] -- Return position of specific number in the puzzle -- the empty space is a zero
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
            self._err.NoTileNumber(nb)
        except Exception as e: print(e)

    def sumManhatanDistance(self, lst: np.array, shape):
        arr = []
        for p in lst:
            score = 0
            pc = np.copy(p)
            for i in range(1, shape * 3, 1):
                item = self.findTileNumber(pc, i)
                goal = (abs(((i- 1) % 3)), abs(int((i - 1) / pc.shape[0])) )
                s = self._score.manhatanDistance(item, goal)
                score += s
            arr.append(score)
        return arr
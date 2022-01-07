import numpy as np
from Puzzle import Puzzle
import random

class CreateBoard():
    def __init__(self):
        self._puzzle = Puzzle()
        pass
    
    def checkGoodPuzzle(self, size):
        return size == (size ** (1/2))**2

    def createPuzzle(self, size, numberShuffle):
        sizeBoard = size + 1
        tier = int(sizeBoard ** (1/2))
        if not(self.checkGoodPuzzle(sizeBoard)): return 84
        solved = np.append(np.arange(1,sizeBoard), np.zeros(1)).reshape(tier, tier).astype(int)
        self.arrayShape = (-1, tier, tier)
        arr = np.array(solved)
        visited = np.array(solved)
        
        for i in range(0, numberShuffle, 1):
            searchSpace = self._puzzle.createAllSwapPossibility(arr, self._puzzle.getSwapPossibility(arr)).reshape(self.arrayShape)
            score = self._puzzle.sumManhatanDistance(searchSpace, tier)
            index = [e for e in range(0, len(score)) if score[e] == score[np.argmax(score)]]
            arr = searchSpace[random.choice(index)]
            visited = np.append(arr, visited).reshape(self.arrayShape)
        return arr


cb = CreateBoard()

arr = cb.createPuzzle(8, 10)

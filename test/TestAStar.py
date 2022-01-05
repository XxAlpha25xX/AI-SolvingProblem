import unittest
import numpy as np
import sys
#print(sys.path)
sys.path.append('../src/InformedSearchAlgorithm/.')
from AStarAlgorithm import AStarAlgorithm

class AStarTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.aS = AStarAlgorithm()
        self.solved8Puzzle = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ])
        self.ex8Puzzle01 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]
        ])
        self.ex8Puzzle02 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [0, 7, 8]
        ])
        self.ex8Puzzle03 = np.array([
            [1, 2, 3],
            [4, 0, 6],
            [7, 5, 8]
        ])

        self.solved24Puzzle = np.array([
            [1,  2,  3,  4,   5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 0],
        ])
        self.ex24Puzzle01 = np.array([
            [1,  2,  3,  4,   5],
            [6,  12,  7,  9,  10],
            [0, 11, 8, 13, 15],
            [16, 17, 18, 14, 19],
            [21, 22, 23, 24, 20],
        ])



    def test_AStarBasic01(self):
        res , history = self.aS.enginePuzzle(iS=self.ex8Puzzle01)
        np.testing.assert_array_equal(res,self.solved8Puzzle)
    def test_AStarBasic02(self):
        res , history = self.aS.enginePuzzle(iS=self.ex8Puzzle02)
        np.testing.assert_array_equal(res,self.solved8Puzzle)
    def test_AStarIntermediate01(self):
        res , history = self.aS.enginePuzzle(iS=self.ex8Puzzle03)
        np.testing.assert_array_equal(res,self.solved8Puzzle)
    
    def test_AStarIntermediate02(self):
        res , history = self.aS.enginePuzzle(iS=self.ex24Puzzle01)
        np.testing.assert_array_equal(res,self.solved24Puzzle)
    
    def printHistory(self, history):
        for tmp in history:
            print(tmp)

if __name__ == '__main__':
    unittest.main()
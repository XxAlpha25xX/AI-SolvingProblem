import unittest
import numpy as np
import sys
#print(sys.path)
sys.path.append('../src/UninformedSearchAlgorithm/.')
from BreadthFirstSearch import BreadthFirstSearch
from Settings import Settings
from Output import Output
class BFSTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.bfs = BreadthFirstSearch()
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

    def test_BreadthFirstSearchBasic01(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=False)
        out = self.bfs.enginePuzzle(state=self.ex8Puzzle01, settings=settings)
        np.testing.assert_array_equal(out.result,self.solved8Puzzle)
    def test_BreadthFirstSearchBasic02(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=False)
        out = self.bfs.enginePuzzle(state=self.ex8Puzzle02, settings=settings)
        np.testing.assert_array_equal(out.result,self.solved8Puzzle)
    def test_BreadthFirstSearchIntermediate(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=False)
        out = self.bfs.enginePuzzle(state=self.ex8Puzzle03, settings=settings)
        np.testing.assert_array_equal(out.result,self.solved8Puzzle)
    
    def printHistory(self, history):
        for tmp in history:
            print(tmp)

if __name__ == '__main__':
    unittest.main()
import unittest
import numpy as np
import sys
#print(sys.path)
sys.path.append('../')
from localSearchAlgorithm import LocalSearchAlgorithm

class LocalSearchAlgorithmTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.lsa = LocalSearchAlgorithm()
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
            [5, 7, 8]
        ])

    def test_basic1(self):
        res , history = self.lsa.hillClimbing(iS=self.ex8Puzzle01)
        np.testing.assert_array_equal(res,self.solved8Puzzle)
    def test_basic2(self):
        res , history = self.lsa.hillClimbing(iS=self.ex8Puzzle02)
        np.testing.assert_array_equal(res,self.solved8Puzzle)
    def test_basic3(self):
        res , history = self.lsa.hillClimbing(iS=self.ex8Puzzle03)
        #print(history)
        np.testing.assert_array_equal(res,self.solved8Puzzle)

if __name__ == '__main__':
    unittest.main()
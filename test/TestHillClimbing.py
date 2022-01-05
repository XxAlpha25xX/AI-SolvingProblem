import unittest
import numpy as np
import sys

from numpy.testing._private.utils import assert_equal
#print(sys.path)
sys.path.append('../src/LocalSearchAlgorithm/.')
from HillClimbing import HillClimbing
from Queen import Queen

class HillClimbingTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.hc = HillClimbing()
        self.queen = Queen()
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
        
        self.ex8Queen04 = np.array([
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                ])

        self.ex8Queen03 = np.array([
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                ])

        self.ex8Queen01 = np.array([
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],        
        ])

        self.ex8Queen02 = np.array([
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1],        
        ])

    def test_hillClimbingPuzzleBasic01(self):
        res , history = self.hc.enginePuzzle(iS=self.ex8Puzzle01)
        np.testing.assert_array_equal(res,self.solved8Puzzle)
    def test_hillClimbingPuzzleBasic02(self):
        res , history = self.hc.enginePuzzle(iS=self.ex8Puzzle03)
        #self.printHistory(history)
        np.testing.assert_array_equal(res,self.solved8Puzzle)
    def test_hillClimbingPuzzleIntermediate(self):
        res , history = self.hc.enginePuzzle(iS=self.ex8Puzzle03)
        #self.printHistory(history)
        np.testing.assert_array_equal(res,self.solved8Puzzle)
    
    def test_hillClimbingQueenBasic01(self):
        res , history = self.hc.engineQueen(board=self.ex8Queen01)
        #self.printHistory(history)
        assert_equal(0, self.queen.sumScore([res]))
    
    def test_hillClimbingQueenBasic02(self):
        res , history = self.hc.engineQueen(board=self.ex8Queen02)
        #self.printHistory(history)
        assert_equal(0, self.queen.sumScore([res]))
    
    def test_hillClimbingQueenIntermediate01(self):
        res , history = self.hc.engineQueen(board=self.ex8Queen03)
        #self.printHistory(history)
        assert_equal(0, self.queen.sumScore([res]))

    def test_hillClimbingQueenIntermediate02(self):
        res , history = self.hc.engineQueen(board=self.ex8Queen04)
        #self.printHistory(history)
        assert_equal(0, self.queen.sumScore([res]))

    def printHistory(self, history):
        for tmp in history:
            print(tmp)

if __name__ == '__main__':
    unittest.main()
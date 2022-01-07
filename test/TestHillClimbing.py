import unittest
import numpy as np
import sys

from numpy.testing._private.utils import assert_equal
#print(sys.path)
sys.path.append('../src/LocalSearchAlgorithm/.')
from HillClimbing import HillClimbing
from Queen import Queen
from Settings import Settings
from Output import Output


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
        
        self.exnQueen04 = np.array([
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
        ])

        self.exnQueen03 = np.array([
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                ])

        self.exnQueen01 = np.array([
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],        
        ])

        self.exnQueen02 = np.array([
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1],        
        ])

        self.exnQueen05 = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])

    def test_hillClimbingPuzzleBasic01(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=False)
        out = self.hc.engine(state=self.ex8Puzzle01, settings=settings)
        np.testing.assert_array_equal(out.result,self.solved8Puzzle)
    def test_hillClimbingPuzzleBasic02(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=False)
        out = self.hc.engine(state=self.ex8Puzzle03, settings=settings)
        np.testing.assert_array_equal(out.result,self.solved8Puzzle)

    def test_hillClimbingPuzzleIntermediate(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=False)
        out = self.hc.engine(state=self.ex8Puzzle03, settings=settings)
        np.testing.assert_array_equal(out.result,self.solved8Puzzle)
    
    def test_hillClimbingQueenBasic01(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=True)
        out = self.hc.engine(state=self.exnQueen01, settings=settings)
        assert_equal(0, self.queen.sumScore([out.result]))
    
    def test_hillClimbingQueenBasic02(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=True)
        out = self.hc.engine(state=self.exnQueen02, settings=settings)
        assert_equal(0, self.queen.sumScore([out.result]))
    
    def test_hillClimbingQueenIntermediate01(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=True)
        out = self.hc.engine(state=self.exnQueen03, settings=settings)
        assert_equal(0, self.queen.sumScore([out.result]))

    def test_hillClimbingQueenIntermediate02(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=True)
        out = self.hc.engine(state=self.exnQueen04, settings=settings)
        assert_equal(0, self.queen.sumScore([out.result]))
    
    def test_hillClimbingQueenHARD01(self):
        settings = Settings(isGraph=False, maxIter=100000, isQueen=True)
        out = self.hc.engine(state=self.exnQueen05, settings=settings)
        assert_equal(0, self.queen.sumScore([out.result]))
    

    def printHistory(self, history):
        for tmp in history:
            print(tmp)

if __name__ == '__main__':
    unittest.main()
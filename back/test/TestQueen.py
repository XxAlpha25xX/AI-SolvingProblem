import unittest
import numpy as np
import sys

from numpy.testing._private.utils import assert_equal

#print(sys.path)
sys.path.append('../lib/.')
from Queen import Queen

class TestQueenMethod(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.queen = Queen()
        self.ex8Queen01 = np.array([
            [1, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0],
        ])

        self.ex8Queen02 = np.array([
            [1, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0],
        ])

    def test_CheckQueenHorizontal01(self):
        res = self.queen.checkQueenHorizontal(self.ex8Queen01, (5, 0))
        assert_equal(res, 3)
    
    def test_CheckQueenHorizontal02(self):
        res = self.queen.checkQueenHorizontal(self.ex8Queen01, (0, 2))
        assert_equal(res, 0)

    def test_CheckQueenVertical01(self):
        res = self.queen.checkQueenVertical(self.ex8Queen01, (6, 6))
        assert_equal(res, 2)
    
    def test_CheckQueenVertical02(self):
        res = self.queen.checkQueenVertical(self.ex8Queen01, (2, 3))
        assert_equal(res, 5)
    
    def test_CheckQueenDiagonal01(self):
        res = self.queen.checkQueenDiagonal(self.ex8Queen01, (1, 1))
        assert_equal(res, 3)
    
    def test_CheckQueenDiagonal02(self):
        res = self.queen.checkQueenDiagonal(self.ex8Queen01, (1, 1))
        assert_equal(res, 3)
    
    def test_CheckQueenDiagonal03(self):
        res = self.queen.checkQueenDiagonal(self.ex8Queen01, (4, 3))
        assert_equal(res, 5)

    def test_CheckQueenAllDirection01(self):
        res = self.queen.checkQueenAllDirection(self.ex8Queen01, (4, 3))
        assert_equal(res, 5)
    
    def test_CheckQueenAllDirection02(self):
        res = self.queen.checkQueenAllDirection(self.ex8Queen02, (4, 3))
        assert_equal(res,10)

if __name__ == '__main__':
    unittest.main()
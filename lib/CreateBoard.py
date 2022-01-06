import numpy as np

class CreateBoard():
    def __init__(self):
        self.x = "???"

    def PuzzleBoardSmall(self):
        arr = np.random.choice(9, 9, replace=False).reshape(3,3)
        return arr

    def PuzzleBoardBig(self):
        arr = np.random.choice(25, 25, replace=False).reshape(5,5)
        return arr

    def QueenBoardSmall(self):
        arr = np.zeros((20, 20), dtype=np.int64)
        return arr

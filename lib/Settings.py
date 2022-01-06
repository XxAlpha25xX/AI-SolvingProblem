class Settings():
    def __init__(self, isGraph: bool, maxIter=100000, isQueen:bool=False) -> None:
        self.isGraph = isGraph
        self.maxIter = maxIter
        self.isQueen = isQueen
        self.isPuzzle = not(self.isQueen)
class Settings():
    def __init__(self, isGraph: bool=False, maxIter=100000, isQueen:bool=False) -> None:
        self.isGraph = isGraph
        self.isTree = not(self.isGraph)
        self.maxIter = maxIter
        self.isQueen = isQueen
        self.isPuzzle = not(self.isQueen)
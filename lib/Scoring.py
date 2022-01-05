import numpy as np

class Move():
    def __init__(self) -> None:
        self.canMoveLeft = False
        self.canMoveRight = False
        self.canMoveUp = False
        self.canMoveDown = False

class Score():
    def __init__(self):
        pass

    def manhatanDistance(self, position, goal):
        return abs(goal[0] - position[0]) + abs(goal[1] - position[1])

    # 0 -> x , 1 -> y
    
        
        
        
        

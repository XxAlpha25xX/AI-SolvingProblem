class Score():
    def __init__(self):
        self.x = "??"

    def manhatanDistance(self, position, goal):
        return abs(goal[0] - position[0]) + abs(goal[1] - position[1])

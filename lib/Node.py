import numpy as np

class Node():
    def __init__(self) -> None:
        self.children = np.array([])
        self.parent = np.array([])
        self.state = np.array([])

    
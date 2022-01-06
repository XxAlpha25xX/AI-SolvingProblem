import numpy as np
import sys
import os
#print(sys.path)

LIB_PATH = os.path.abspath(os.getcwd()) + '/../lib/'
sys.path.append(LIB_PATH)
from Error import ErrorCodex as Err
from Scoring import Score as Score
from Puzzle import Puzzle as Puzzle
from Queen import Queen as Queen
from Node import Node as Node
from Settings import Settings
import random

class HillClimbing():

    # [blank] -- Init
    def __init__(self):
        self.expectedShape = np.array([(3, 3), (5, 5)])
        self._err = Err()
        self._score = Score()
        self._puzzle = Puzzle()
        self._queen = Queen()
    
    def initVar(self, iS: np.array):
        self.size = iS.shape[0]
        self.shape = (self.size, self.size)
        self.arrayShape = (-1, self.size, self.size)
        self.len = self.size * self.size

    # [np.array] -- Try to find the local maxima
    def engine(self, state: np.array, settings: Settings) -> np.array:
        try:
            visited = np.array([state])
            searchSpace = np.array([])
            score = 0
            maxima = False
            iterations = 0

            if state.shape[0] != state.shape[1]: self._err.IncorrectNumpyShape()
            self.initVar(state)
            while not(maxima):
                if settings.isPuzzle : searchSpace = self._puzzle.createAllSwapPossibility(state, self._puzzle.getSwapPossibility(state)).reshape(self.arrayShape)
                elif settings.isQueen: searchSpace = self._queen.createAllMovePossible(state)
                if not(settings.isGraph) and visited.shape[0] > 0:
                    tmp = [i for i, search in enumerate(searchSpace) for state in visited if np.array_equal(state, search)]
                    searchSpace = np.delete(searchSpace, tmp, axis=0).reshape(self.arrayShape)
                if settings.isPuzzle : score = self._puzzle.sumManhatanDistance(searchSpace, self.size)
                elif settings.isQueen: score = self._queen.sumScore(searchSpace)
                index = [e for e in range(0, len(score)) if score[e] == score[np.argmin(score)]]
                state = searchSpace[random.choice(index)]
                visited = np.append(visited, state).reshape(self.arrayShape)
                iterations += 1
                if score[np.argmin(score)] == 0: maxima = True
                elif iterations > settings.maxIter: maxima = True
            return state, visited
        except Exception as e: 
            print("🧐[Error][Exceptions raised] ")
            print(e)
            return None, []

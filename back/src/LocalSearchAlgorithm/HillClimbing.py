import numpy as np
import sys
import os
import json
#print(sys.path)

LIB_PATH = os.path.abspath(os.getcwd()) + '/../lib/'
sys.path.append(LIB_PATH)
from Error import ErrorCodex as Err
from Scoring import Score as Score
from Puzzle import Puzzle as Puzzle
from Queen import Queen as Queen
from Node import Node as Node
from Settings import Settings
from Output import Output
import random

class HillClimbing():

    # [blank] -- Init
    def __init__(self):
        self.expectedShape = np.array([(3, 3), (5, 5)])
        self._err = Err()
        self._node = Node()
        self._score = Score()
        self._puzzle = Puzzle()
        self._queen = Queen()
    
    def initVar(self, iS: np.array):
        self.size = iS.shape[0]
        self.shape = (self.size, self.size)
        self.arrayShape = (-1, self.size, self.size)
        self.len = self.size * self.size

    # [np.array] -- Try to find the local maxima
    def engine(self, state: np.array, settings: Settings) -> Output:
        try:
            # [Init Variables] -- Scope
            visited = np.array([state])
            tree = {"id": self._node.npToString(state), "children": []} #
            graph = {"nodes" : [{"id":self._node.npToString(state)}], "links": []}
            searchSpace = np.array([])
            score = 0
            maxima = False
            iterations = 0

            # [TO DO] -- Need to  check if already solve
            if state.shape[0] != state.shape[1]: self._err.IncorrectNumpyShape() # [Error Management] -- Bad Shape
            self.initVar(state) # [Init Variables] -- Reusable variable
            while not(maxima):
                #[Puzzle] -- Create all move possible
                if settings.isPuzzle : searchSpace = self._puzzle.createAllSwapPossibility(state, self._puzzle.getSwapPossibility(state)).reshape(self.arrayShape)
                #[Queen] -- Create all move possible
                elif settings.isQueen: searchSpace = self._queen.createAllMovePossible(state)
                #[Tree Mode] -- Delete all already visited states
                if not(settings.isGraph) and visited.shape[0] > 0:
                    tmp = [i for i, search in enumerate(searchSpace) for state in visited if np.array_equal(state, search)]
                    searchSpace = np.delete(searchSpace, tmp, axis=0).reshape(self.arrayShape)
                #[Puzzle] -- Determine local maxima
                if settings.isPuzzle : score = self._puzzle.sumManhatanDistance(searchSpace, self.size)
                #[Queen] -- Determine local maxima
                elif settings.isQueen: score = self._queen.sumScore(searchSpace)
                #[Algorithm] -- Pick random local maxima in order to avoid loop                
                index = [e for e in range(0, len(score)) if score[e] == score[np.argmin(score)]]
                newState = searchSpace[random.choice(index)]
                #[Tree Mode] -- Add Leaves in tree
                if not(settings.isGraph): self._node.addTreeChildren(self._node.findIdNodeInTree(tree, self._node.npToString(state)), self._node.npToString(newState))
                #[Graph Mode ] -- Add Node and edges in graph
                elif settings.isGraph: self._node.graphHandle(graph, self._node.npToString(state), self._node.npToString(newState))
                #[Algorithm] -- Update state based on local maxima
                state = newState
                #[Algorithm] -- Add the new state to visited list
                visited = np.append(visited, state).reshape(self.arrayShape)
                iterations += 1
                #[Algorithm] -- Check if already solves
                if score[np.argmin(score)] == 0: maxima = True
                #[Algorithm] -- Check if maximum moves have been reached
                elif iterations > settings.maxIter: maxima = True
            #print(json.dumps(tree, indent=4))
            #print(json.dumps(graph, indent=4))
            return Output(res=state, history=visited, settings=settings, graph=graph, tree=tree)
        except Exception as e: 
            print("🧐[Error][Exceptions raised]")
            print(e)
            return None, []


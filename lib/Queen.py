from logging import error
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from Error import ErrorCodex as Error

ITEM_QUEEN = 1

class Queen():

    def __init__(self) -> None:
        self.err = Error()

    def getAllQueenPosition(self, board: np.array):
        arr = []
        x = 0
        y = 0

        for column in board:
            x = 0
            for row in column:
                if row == ITEM_QUEEN: arr.append((x, y))
                x += 1
            y += 1
        return arr

    # pos {x -> [0] / y -> [1]}
    def checkQueenHorizontal(self, board: np.array, pos: tuple[int, int]):
        x = pos[0]
        y = pos[1]
        size = board.shape[0]
        score = 0

        for xi in range(x + 1, size, 1):
            if board[y][xi] == ITEM_QUEEN: score += 1
        for xi in range(x - 1, - 1, -1):
            if board[y][xi] == ITEM_QUEEN: score += 1
        return score

    def checkQueenVertical(self, board: np.array, pos: tuple[int, int]):
        x = pos[0]
        y = pos[1]
        size = board.shape[0]
        score = 0

        for yi in range(y + 1, size, 1):
            if board[yi][x] == ITEM_QUEEN: score += 1
        for yi in range(y - 1, - 1, -1):
            if board[yi][x] == ITEM_QUEEN: score += 1
        return score

    def checkQueenDiagonal(self, board: np.array, pos: tuple[int, int]):
        x = pos[0]
        y = pos[1]
        size = board.shape[0]
        score = 0

        #Down - Right
        for xi, yi in zip(range(x + 1, size, 1), range(y + 1, size, 1)):
            if board[yi][xi] == ITEM_QUEEN: score += 1
        #Up - Left
        for xi, yi in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
            if board[yi][xi] == ITEM_QUEEN: score += 1
        #Down- Left
        for xi, yi in zip(range(x - 1, -1, -1), range(y + 1, size, 1)):
            if board[yi][xi] == ITEM_QUEEN: score += 1
        #Up - Right
        for xi, yi in zip(range(x + 1, size, 1), range(y - 1, -1, -1)):
            if board[yi][xi] == ITEM_QUEEN: score += 1
        return score

    def checkQueenAllDirection(self, board: np.array, pos: tuple[int, int]):
        return self.checkQueenHorizontal(board,pos) + self.checkQueenVertical(board, pos) + self.checkQueenDiagonal(board, pos)

    def moveQueenTo(self, iS: np.array, pos1: tuple[int, int], pos2: tuple[int, int]) -> np.array:
        try:
            tmp = iS[pos1[1]][pos1[0]]
            iS[pos1[1]][pos1[0]] = iS[pos2[1]][pos2[0]]
            iS[pos2[1]][pos2[0]] = tmp
            return iS
        except Exception as e: print(e)
    
    # pos {x -> [0] / y -> [1]}
    def getQueenMovePossibility(self, board: np.array, pos: tuple[int, int]) -> np.array:
        try:
            arr = []
            size = board.shape[0]
            
            #print("Pos232", pos)
            #print("Board232\n", board)

            if board[pos[1]][pos[0]] != ITEM_QUEEN: self.err.NoQueenFound(pos)

            #Left-Right-[1-8]
            for xi in range(pos[0] + 1, size, 1):
                if board[pos[1]][xi] != ITEM_QUEEN: arr.append( (xi, pos[1]) )
            for xi in range(pos[0] - 1, - 1, -1):
                if board[pos[1]][xi] != ITEM_QUEEN: arr.append( (xi, pos[1]) )
            #Left
            #if pos[0] - 1 >= 0 and board[pos[1]][pos[0] - 1] != ITEM_QUEEN: arr.append( (pos[0] - 1, pos[1]) )
            #Right
            #if pos[0] + 1 < size and board[pos[1]][pos[0] + 1] != ITEM_QUEEN: arr.append( (pos[0] + 1, pos[1]) )

            #Up-Down-[1-8]
            for yi in range(pos[1] + 1, size, 1):
                if board[yi][pos[0]] != ITEM_QUEEN: arr.append( (pos[0], yi) )
            for yi in range(pos[1] - 1, - 1, -1):
                if board[yi][pos[0]] != ITEM_QUEEN: arr.append( (pos[0], yi) )
            #Up
            if pos[1] - 1 >= 0 and board[pos[1] - 1][pos[0]] != ITEM_QUEEN: arr.append( (pos[0], pos[1] - 1) )
            #Down
            if pos[1] + 1 < size and board[pos[1] + 1][pos[0]] != ITEM_QUEEN: arr.append( (pos[0], pos[1] + 1) )
            #Down - Left
           # if (pos[1] + 1 < size and pos[0] - 1 >= 0) and (board[pos[1] + 1][pos[0] - 1] != ITEM_QUEEN): arr.append( (pos[0] - 1, pos[1] + 1) )
            #Down - Right
           # if (pos[1] + 1 < size and pos[0] + 1 < size) and (board[pos[1] + 1][pos[0] + 1] != ITEM_QUEEN): arr.append( (pos[0] + 1, pos[1] + 1) )
            #Up - Left
           # if (pos[1] - 1 >= 0 and pos[0] - 1 >= 0) and (board[pos[1] - 1][pos[0] - 1] != ITEM_QUEEN): arr.append( (pos[0] - 1, pos[1] - 1) )
            #Up - Right
           # if (pos[1] - 1 >= 0 and pos[0] + 1 < size) and (board[pos[1] - 1][pos[0] + 1] != ITEM_QUEEN): arr.append( (pos[0] + 1, pos[1] - 1) )
            return arr
        except Exception as e: 
            print(e)
            return 84
    
    def createAllMovePossible(self, board: np.array):
        try:
            arr = np.array([])
            size = board.shape[0]
            boardCpy = np.copy(board)
            queens = self.getAllQueenPosition(boardCpy)

            for queen in queens:
                moves = self.getQueenMovePossibility(boardCpy, queen)
                for move in moves:
                    possible = np.copy(self.moveQueenTo(boardCpy, move, queen).astype(int))
                    arr = np.append(arr, possible)
                    boardCpy = np.copy(board).astype(int)
            arr = arr.reshape((-1, size, size)).astype(int)
            return arr
        except Exception as e: 
            print(e)
            return 84
    
    def sumScore(self, boards: np.array):
        arr = np.array([])
        for board in boards:
            score = 0  
            queens = self.getAllQueenPosition(board)
            for tmp in queens: score += self.checkQueenAllDirection(board, tmp)
            arr = np.append(arr, score)
        return arr
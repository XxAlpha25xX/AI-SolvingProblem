class ErrorCodex():
    def __init__(self):
        self.x = "???"

    def IncorrectNumpyShape(self, inputT, expected):
        message = "[Error] The shape receive as argument is incorrect\n"
        raise Exception(message)
    
    def NoTileNumber(self, number):
        message = "[Error] No tile (" + str(number) +  ") have been found on the puzzle\n" 
        raise Exception(message)

    def BFSQueueEmpty(self):
        message = "[Error] The BFS queue is empty\n" 
        raise Exception(message)
    
    def NoQueenFound(self, pos):
        inputStr = '(' + ','.join([str(e) for e in pos]) + ')'
        message = "[Error] The queen was not found at " + inputStr + "\n" 
        raise Exception(message)
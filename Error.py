class ErrorCodex():
    def __init__(self):
        self.x = "???"

    def IncorrectNumpyShape(self, inputT, expected):
        expectedStr = ', or '.join([str(e) for e in expected])
        inputStr = '(' + ''.join([str(e) for e in inputT]) + ')'
        message = "[Error] The shape receive as argument is incorrect\n"
        message += "\t {Expected} :" + expectedStr + "\n"
        message += "\t {Received} :" + inputStr + "\n"
        raise Exception(message)
    
    def NoTileNumber(self, number):
        message = "[Error] No tile (" + str(number) +  ") have been found on the puzzle" 
        raise Exception(message)
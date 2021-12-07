from typing import List
bingos = []
bingosValues = []
class BingoNumber:
    def __init__(self, value):
        self.showed = False
        self.value = value

    def show(self):
        self.showed = True
    
    def __repr__(self):
        return "( " + str(self.value) + ", " + str(self.showed) + " )"

class BingoCard:
    def __init__(self, board):
        global bingosValues, bingos
        self.board = [[0 for x in range(5)] for y in range(5)]
        rows = board.split('\n')
        if (len(rows) > 5):
            rows = rows[len(rows) - 5:]
        for i in range(len(rows)):
            values = list(map(lambda x: int(x), rows[i].split()))
            for j in range(len(values)): 
                if values[j] not in bingosValues:
                    bingosValues.append(values[j])
                    bingos.append(BingoNumber(values[j]))
                self.board[i][j] = list(filter(lambda x: x.value == values[j], bingos))[0]
                print

    def bingo(self):
        for i in range(len(self.board)):
            if all(v.showed for v in self.board[i]):
                return True
            column = list(map(lambda x: x[i], self.board))
            if all(v.showed for v in column):
                return True
    
    def getRemaining(self):
        result = 0
        for i in range(len(self.board)):
            result += sum( n.value for n in self.board[i] if not n.showed)
        return result



def readData(sample = False) -> List[str]:
    global bingos, bingosValues
    filename = "./sample.txt" if sample else "./data.txt"
    f = open(filename, "r")
    firstRow =  f.readline().split(',')
    bingos = list(map(lambda x: BingoNumber(int(x)), firstRow))
    bingosValues = list(map(lambda x: int(x), firstRow))
    boards = list(map(lambda x: BingoCard(x), ''.join(f.readlines()).split("\n\n")))
    return boards

def getFastestResult(boards):
    for number in bingos:
        number.show()
        for board in boards:
            if board.bingo():
                return number.value * board.getRemaining()

def getSlowestResult(boards):
    for number in bingos:
        number.show()
        for board in boards:
            if board.bingo():
                if (len(boards) > 1):
                    boards.remove(board)
                else:
                    return number.value * board.getRemaining()


print(getFastestResult(readData()))
print(getSlowestResult(readData(True)))
print(getSlowestResult(readData()))
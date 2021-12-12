from typing import List

sample = [["forward", "5"], ["down", "5"], ["forward", "8"], ["up", "3"], ["down", "8"], ["forward", "2"]]

class Command: 
    def __init__(self, commandLine):
        self.command = commandLine[0]
        self.step = int(commandLine[1])
    
    def isForward(self):
        return self.command == "forward"

    def isUp(self):
        return self.command == "up"

    def isDown(self):
        return self.command == "down"

sample = list(map(lambda x: Command(x), sample))

def readData() -> List[Command]:
    f = open("./data.txt", "r")
    values = list(map(lambda x: Command(x.replace("\n", "").split()), f.readlines()))
    f.close()
    return values

def getCoordinates(commands: List[Command]):
    depth = 0
    horizontal = 0
    for com in commands:
        if com.isForward(): 
            horizontal += com.step
        if com.isUp():
            depth -= com.step
        if com.isDown():
            depth += com.step
    return horizontal * depth

def getFinalCoordinates(commands: List[Command]):
    aim = 0
    depth = 0
    horizontal = 0
    for com in commands:
        if com.isForward(): 
            horizontal += com.step
            depth += aim * com.step
        if com.isUp():
            aim -= com.step
        if com.isDown():
            aim += com.step
    return horizontal * depth

print(getFinalCoordinates(sample))
print(getFinalCoordinates(readData()))
from typing import List

openingChar = ['(', '[', '{', '<']
closingChar = [')', ']', '}', '>']
closingValues = {')': 3, ']': 57, '}': 1197, '>': 25137}
openingValues = {'(': 1, '[': 2, '{': 3, '<': 4}

def groupBy(lst): 
    count = {}
    for element in lst:
        if element not in count:
            count[element] = 0
        count[element] += 1
    return count

def readData(sample = False) -> List[str]:
    filename = "./sample.txt" if sample else "./data.txt"
    f = open(filename, "r")
    lines = list(map(lambda x: x.rstrip('\n'), f.readlines()))
    f.close()
    return lines

def scanCorruptedLine(line):
    queue = []
    for char in line:
        if char in openingChar:
            queue.append(char)
        elif char in closingChar:
            opening = queue.pop()
            oIndex = openingChar.index(opening)
            if (char != closingChar[oIndex]):
                return closingValues[char]
    return 0

def getCorruptedResult(lines):
    result = 0
    for line in lines:
        result += scanCorruptedLine(line)
    return result

def scanMissingLine(line):
    queue = []
    result = 0
    for char in line:
        if char in openingChar:
            queue.append(char)
        elif char in closingChar:
            opening = queue.pop()
            oIndex = openingChar.index(opening)
            if (char != closingChar[oIndex]):
                return result
    for i in range(len(queue)-1, -1, -1):
        result = (result * 5)+ openingValues[queue[i]]
    return result

def getMissingResult(lines):
    result = []
    for line in lines:
        res = scanMissingLine(line)
        if (res != 0):
            result.append(res)
    result.sort()
    return result[len(result)//2]

print(getCorruptedResult(readData(True)))
print(getCorruptedResult(readData()))
print(getMissingResult(readData(True)))
print(getMissingResult(readData()))
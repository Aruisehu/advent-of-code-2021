from typing import List

class AreaPoint:
    def __init__(self, value, i, j):
        self.i = i
        self.j = j
        self.value = value
    
    def __repr__(self):
        return f"AP({self.value}, {self.i}/{self.j})"

    def __hash__(self):
        return hash(f"AP({self.value}, {self.i}/{self.j})")

    def __eq__(self, __o: object) -> bool:
        return __o.__hash__() == self.__hash__()

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
    lines = list(map(lambda x: list(map(lambda y: int(y), list(x.rstrip('\n')))), f.readlines()))
    f.close()
    return lines

def getAllRisk(points):
    result = 0
    for point in points:
        result += point.value + 1
    return result

def isLowest(points, i, j):
    result = True
    if (i < len(points)-1):
        result = result and points[i][j] < points[i+1][j]
    if (i > 0):
        result = result and points[i][j] < points[i-1][j]
    if (j < len(points[0])-1):
        result = result and points[i][j] < points[i][j+1]
    if (j > 0):
        result = result and points[i][j] < points[i][j-1]
    return result

def newAreaPoints(points, i, j):
    result = []
    if (i < len(points)-1):
        if points[i+1][j] < 9:
            result.append(AreaPoint(points[i+1][j], i+1, j))
    if (i > 0):
        if points[i-1][j] < 9:
            result.append(AreaPoint(points[i-1][j], i-1, j))
    if (j < len(points[0])-1):
        if points[i][j+1] < 9:
            result.append(AreaPoint(points[i][j+1], i, j+1))
    if (j > 0):
        if points[i][j-1] < 9:
            result.append(AreaPoint(points[i][j-1], i, j-1))
    return result

def getLowestPoints(points):
    result = []
    for i in range(len(points)):
        for j in range(len(points[i])):
            if isLowest(points, i, j):
                result.append(AreaPoint(points[i][j], i, j))
    return result

def getAreas(points):
    areas = []
    lowest = getLowestPoints(points)
    for low in lowest:
        res = []
        remaining = [low]
        while len(remaining) > 0:
            curr = remaining.pop(0)
            new = newAreaPoints(points, curr.i, curr.j)
            res.append(curr)
            for i in res:
                if i in new:
                    new.remove(i)
            remaining.extend(new)
        res = list(set(res))
        areas.append(res)
    return areas

def getResult(points):
    return getAllRisk(getLowestPoints(points))

def getAreaResult(points):
    res = 1
    areas = getAreas(points)
    areas.sort(key=len, reverse=True)
    for i in range(3):
        res *= len(areas[i])
    return res

print(getResult(readData(True)))
print(getResult(readData()))
print(getAreaResult(readData(True)))
print(getAreaResult(readData()))

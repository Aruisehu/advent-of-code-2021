from typing import List

class Coord: 
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __repr__(self):
        return f"c({self.x}, {self.y})"
    
    def __eq__(self, c) -> bool:
        return self.x == c.x and self.y == c.y
    
    def __ne__(self, c) -> bool:
        return self.x != c.x or self.y != c.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Vent:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
        self.points = []
        self.__inBetweenPoint()
    
    def __repr__(self):
        return f"v({self.c1} -> {self.c2})"
    
    def __inBetweenPoint(self):
        diffX = self.c1.x - self.c2.x
        diffY = self.c1.y - self.c2.y
        if (diffX == 0):
            mini = min(self.c1.y, self.c2.y)
            maxi = max(self.c1.y, self.c2.y) + 1
            for i in range(mini, maxi):
                self.points.append(Coord(self.c1.x, i))
        elif (diffY == 0):
            mini = min(self.c1.x, self.c2.x)
            maxi = max(self.c1.x, self.c2.x) + 1
            for i in range(mini, maxi):
                self.points.append(Coord(i, self.c1.y))
        elif (abs(diffX) == abs(diffY)):
            signX = -diffX / abs(diffX)
            signY = -diffY / abs(diffY)
            for i in range(abs(diffX) + 1):
                self.points.append(Coord(self.c1.x + (i * signX), self.c1.y + (i * signY)))

def groupBy(lst): 
    count = {}
    for element in lst:
        if element not in count:
            count[element] = 0
        count[element] += 1
    return count

def readData(sample = False) -> List[str]:
    global bingos, bingosValues
    filename = "./sample.txt" if sample else "./data.txt"
    f = open(filename, "r")
    vents = list(map(lambda x: createVent(x), f.readlines()))
    f.close()
    return vents

def createVent(line):
    rawCoords = line.split(" -> ")
    coord1 = rawCoords[0].split(',')
    coord2 = rawCoords[1].split(',')
    return Vent(Coord(coord1[0], coord1[1]), Coord(coord2[0], coord2[1]))

def getOverlappingPointsCount(vents):
    coords = []
    for vent in vents: 
        coords.extend(vent.points)
    groups = groupBy(coords)
    return len(dict(filter(lambda x: x[1] > 1, groups.items())))

print(getOverlappingPointsCount(readData(True)))
print(getOverlappingPointsCount(readData()))
    
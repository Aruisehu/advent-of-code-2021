from typing import List

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
    crabs = list(map(lambda x: int(x), f.readline().rstrip("\n").split(',')))
    f.close()
    return crabs

def getTriangular(n):
    return int(n * (n + 1) / 2)

def getFuelConsumedForPos(crabs, pos):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - pos)
    return fuel

def getFuelConsumedForTriangularPos(crabs, pos):
    fuel = 0
    for crab in crabs:
        fuel += getTriangular(abs(crab - pos))
    return fuel

def getSmallestFuel(crabs):
    mini = min(crabs)
    maxi = max(crabs)
    smallest = getFuelConsumedForPos(crabs, maxi + 1)
    pos = maxi + 1
    for i in range(mini, maxi):
        val = getFuelConsumedForPos(crabs, i)
        if (val < smallest):
            pos = i
            smallest = val
    return (pos, smallest)

def getSmallestTriangularFuel(crabs):
    mini = min(crabs)
    maxi = max(crabs)
    smallest = getFuelConsumedForTriangularPos(crabs, maxi + 1)
    pos = maxi + 1
    for i in range(mini, maxi):
        val = getFuelConsumedForTriangularPos(crabs, i)
        if (val < smallest):
            pos = i
            smallest = val
    return (pos, smallest)


print(getSmallestFuel(readData(True)))
print(getSmallestFuel(readData()))
print(getSmallestTriangularFuel(readData(True)))
print(getSmallestTriangularFuel(readData()))
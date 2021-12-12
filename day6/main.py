from typing import List

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
    lanterns = list(map(lambda x: int(x), f.readline().rstrip("\n").split(',')))
    f.close()
    return lanterns

def normalizeLanterns(lanterns):
    for i in range(9):
        if i not in lanterns:
            lanterns[i] = 0
    return lanterns

    
def passDay(lanterns):
    newLanterns = lanterns.copy()
    for i in range(8,-1, -1):
        if (i == 0):
            newLanterns[6] += lanterns[0]
        newIndex = (i - 1) % 9
        newLanterns[newIndex] = lanterns[i]
    return newLanterns

def passNDays(lanterns, n):
    lanterns = normalizeLanterns(groupBy(lanterns))
    for _ in range(n):
        lanterns = passDay(lanterns)
    return lanterns

print(sum(list(passNDays(readData(True), 18).values())))
print(sum(list(passNDays(readData(True), 80).values())))
print(sum(list(passNDays(readData(), 80).values())))
print(sum(list(passNDays(readData(), 256).values())))

        
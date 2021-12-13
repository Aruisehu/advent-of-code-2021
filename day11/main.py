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
    lines = list(map(lambda x: list(map(lambda y: int(y), list(x.rstrip('\n')))), f.readlines()))
    f.close()
    return lines

def passStep(takodachis):
    nbFlashes = 0
    totalFlashes = []
    # step 1: Increase
    for i in range(10):
        for j in range(10):
            takodachis[i][j] += 1
    
    # step 2: Flash
    hasFlash = True
    while (hasFlash):
        flashes = []
        hasFlash = False
        for i in range(10):
            for j in range(10):
                if takodachis[i][j] > 9 and (i, j) not in totalFlashes:
                    hasFlash = True
                    nbFlashes += 1
                    flashes.append((i, j))

        for flash in flashes:
            i = flash[0]
            j = flash[1]
            for di in range(-1,2):
                if (i+di < 0 or i+di > 9):
                    continue
                for dj in range(-1,2):
                    if (j+dj < 0 or j+dj > 9 or (di == 0 and dj == 0)):
                        continue
                    takodachis[i+di][j+dj] += 1
        totalFlashes.extend(flashes)
    
    # Step 3 reset flashes    
    for flash in totalFlashes:
        i = flash[0]
        j = flash[1]
        takodachis[i][j] = 0
    
    return (takodachis, nbFlashes)

def passNStep(takodachis, n):
    total = 0
    for i in range(n):
        result = passStep(takodachis)
        takodachis = result[0]
        total += result[1]
    return total

def findFirstStepWhereAllFlash(takodachis):
    nbStep = 0
    while True:
        nbStep += 1
        result = passStep(takodachis)
        takodachis = result[0]
        if result[1] == 100:
            return nbStep

print(passNStep(readData(True), 100))
print(passNStep(readData(), 100))
print(findFirstStepWhereAllFlash(readData(True)))
print(findFirstStepWhereAllFlash(readData()))
                
        
    


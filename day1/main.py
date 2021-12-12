sample = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def readData():
    f = open("./data.txt", "r")
    values = list(map(lambda x: int(x.replace("\n", "")), f.readlines()))
    f.close()
    return values

def getIncreases(lst): 
    increases = 0;
    prev = lst[0]
    for i in range(1, len(lst)):
        curr = lst[i]
        if curr > prev:
            increases += 1
        prev = curr
    return increases

def getSlidingSum(lst, factor):
    result = []
    for i in range(len(lst) - factor +1):
        sum = 0
        for j in range(factor):
            sum += lst[i+j]
        result.append(sum)
    return result

def getSlidingIncreases(lst, factor):
    slidingSum = getSlidingSum(lst, factor)
    return getIncreases(slidingSum)

print(getSlidingIncreases(readData(), 3))
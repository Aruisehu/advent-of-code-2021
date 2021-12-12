from typing import List

sample = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

def readData() -> List[str]:
    f = open("./data.txt", "r")
    values = list(map(lambda x: x.replace("\n", ""), f.readlines()))
    f.close()
    return values

def countBits(bits): 
    count = {}
    for bit in bits:
        if bit not in count:
            count[bit] = 0
        count[bit] += 1
    return count

def getGamma(bytes):
    # Assume all values has the same number of bits
    gamma = ""
    for i in range(len(bytes[0])):
        bits = list(map(lambda x: x[i], bytes))
        count = countBits(bits)
        gamma += max(count, key=count.get)
    return gamma

def getEpsilonFromGamma(gamma):
    epsilon = ""
    for bit in gamma:
        epsilon += "0" if bit == "1" else "1"
    return epsilon

def getResult(bytes):
    gamma = getGamma(bytes)
    epsilon = getEpsilonFromGamma(gamma)
    return int(gamma, 2) * int(epsilon, 2)

def getOxygen(bytes):
    remaining = bytes
    maxLoop = len(bytes[0])
    for i in range(maxLoop):
        bits = list(map(lambda x: x[i], remaining))
        count = countBits(bits)
        mostCommonBit = "0" if count["0"] > count["1"] else "1"
        remaining = list(filter(lambda x: x[i] == mostCommonBit, remaining))       
        if (len(remaining) == 1):
            return int(remaining[0], 2)


def getCO2(bytes):
    remaining = bytes
    maxLoop = len(bytes[0])
    for i in range(maxLoop):
        bits = list(map(lambda x: x[i], remaining))
        count = countBits(bits)
        leastCommonBit = "0" if count["1"] >= count["0"]  else "1"
        remaining = list(filter(lambda x: x[i] == leastCommonBit, remaining))
        if (len(remaining) == 1):
            return int(remaining[0], 2)

print(getResult(sample))
print(getResult(readData()))
print(getOxygen(sample))
print(getOxygen(readData()))
print(getCO2(sample))
print(getCO2(readData()))
print(getOxygen(readData()) * getCO2(readData()))
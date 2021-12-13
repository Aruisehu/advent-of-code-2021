from typing import List

class Recognized: 
    def __init__(self, value, string):
        self.value = value
        self.string = string
        self.length = len(string)
        self._setString = set(string)
    
    def inCommon(self, string):
        return len(self._setString.intersection(set(string)))
    
    def isIdentical(self, string):
        newSet = set(string)
        return self._setString.issubset(newSet) and self._setString.issuperset(newSet)
        
    def isSubset(self, string):
        return self._setString.issubset(set(string))

    def isSuperset(self, string):
        return self._setString.issuperset(set(string))

    def __repr__(self):
        return f"R({self.value}, {self.string})"

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
    lines = list(map(lambda x: (x.split(' | ')[0].split(), x.split(' | ')[1].split()), f.readlines()))
    f.close()
    return lines

def read1478InOutput(lines):
    nbInst = 0
    for line in lines:
        for digit in line[1]:
            if len(digit) in [2, 3, 4 ,7]:
                nbInst += 1
    return nbInst

def buildRecognizedList(lst):
    copyList = list(lst)
    recognized = {}
    for number in copyList:
        if (len(number) == 2):
            recognized[1] = Recognized(1, number)
        elif (len(number) == 4):
            recognized[4] = Recognized(4, number)
        elif (len(number) == 3):
            recognized[7] = Recognized(7, number)
        elif (len(number) == 7):
            recognized[8] = Recognized(8, number)
        
    for number in copyList:
        # Build 2, 3 and 5 from 1 4 7 8
        if len(number) == 5:
            if (recognized[4].inCommon(number) == 3 and recognized[1].inCommon(number) == 1):
                recognized[5] = Recognized(5, number)
            elif (recognized[4].inCommon(number) == 2 and recognized[1].inCommon(number) == 1):
                recognized[2] = Recognized(2, number)
            elif (recognized[4].inCommon(number) == 3 and recognized[1].isSubset(number)):
                recognized[3] = Recognized(3, number)
    for number in copyList:
        # Build 0, 6, 9 from 1 2 3 4 5 7 8
        if len(number) == 6 :
            if (recognized[5].isSubset(number) and recognized[1].isSubset(number)):
                recognized[9] = Recognized(9, number)
            elif (recognized[5].isSubset(number) and recognized[1].inCommon(number) == 1):
                recognized[6] = Recognized(6, number)
            elif (recognized[2].inCommon(number) == 4 and recognized[1].isSubset(number)):
                recognized[0] = Recognized(0, number)
    return list(recognized.values())       

def getNumberFromRecognize(number, recognize):
    for recon in recognize:
        if (recon.isIdentical(number)):
            return recon.value
        

def getResult(lines):
    res = 0
    for line in lines:
        curNum = 0
        recognize = buildRecognizedList(line[0])    
        for output in line[1]:
            curNum = curNum * 10 + getNumberFromRecognize(output, recognize)
        res += curNum
    return res

print(read1478InOutput(readData(True)))
print(read1478InOutput(readData()))
print(getResult(readData(True)))
print(getResult(readData()))
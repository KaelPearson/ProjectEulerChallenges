import time

def getSumOfDigits(num):
    sumOfDigits = 0
    for i in str(num):
        sumOfDigits += int(i)
    return sumOfDigits
factorialArr = [0,1,2,6,24,120,720,5040,40320,362880]
def getSumOfFactorialDigits(num):
    total = 0
    for i in str(num):
        total += factorialArr[int(i)]
    return total

def getf(num):
    return getSumOfFactorialDigits(num)
def getsf(num):
    return getSumOfDigits(getSumOfFactorialDigits(num))
def getSpecificg(num):
    currNum = 1
    while(True):
        if(getsf(currNum) == num):
            return currNum
        currNum += 1
def getg(limit):
    gList = []
    for i in range(0,limit):
        gList.append(0)
    spot = 1
    while(True):
        for i in range(0,len(gList)):
            if(gList[i] == 0):
                break
            elif(i == (len(gList) - 1)):
                return gList
        spotsf = getsf(spot)
        if(spotsf <= limit):
            if(gList[spotsf - 1] == 0):
                gList[spotsf - 1] = spot
        spot += 1
def addArr(arr):
    sum = 0
    for i in arr:
        sum += getSumOfDigits(i)
    return sum
def check(limit):
    sum = 0
    for i in range(1,limit + 1):
        g = getSumOfDigits(getSpecificg(i))
        sum += g
    return sum
def getallf(limit):
    fArr = []
    for i in range(0,(limit+1)):
        fArr.append(getf(i))
    return fArr
def getallsf(limit):
    sfArr = []
    for i in range(0,(limit+1)):
        sfArr.append(getsf(i))
    return sfArr
def getallsg(limit):
    sgArr = []
    for i in range(1,(limit+1)):
        sgArr.append(getSumOfDigits(getSpecificg(i)))
    return sgArr
def main():
    seconds = time.time()
    print(getallf(45))
    seconds2 = time.time()
    print(seconds2 - seconds, " time taken")

if(__name__ == "__main__"):
    main()
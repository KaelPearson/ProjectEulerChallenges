import time
allSums = []
amicable = []
def getSumDivisors(num):
    divs = [1]
    for i in range(2,int(num/2) + 1):
        if(num % i == 0):
            divs.append(i)
    return addArr(divs)
def addArr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
def getSumDivisorsToLimit(limit):
    for i in range(1,limit+1):
        allSums.append(getSumDivisors(i))
    return allSums
def checkAmicable():
    for i in range(len(allSums)):
        for k in range(len(allSums)):
            if(allSums[k] == i+1 and allSums[i] == k+1 and allSums[k] != allSums[i]):
                amicable.append(allSums[k])
                amicable.append(allSums[i])
                allSums[k] = 0
        allSums[i] = 0
    return amicable
def main():
    seconds = time.time()
    getSumDivisorsToLimit(4000)
    print(addArr(checkAmicable()))
    seconds2 = time.time()
    print(seconds2 - seconds)

if(__name__ == "__main__"):
    main()
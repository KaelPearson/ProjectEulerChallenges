import math
import time

def getAllAbundantNums(limit):
    abundantNums = []
    for i in range(1, limit+1):
        if(getSumOfDivisors(i) > i):
            abundantNums.append(i)
    return abundantNums

def getSumOfDivisors(num):
    sum = 1
    for i in range(2,int(math.sqrt(num) + 1)):
        if(num % i == 0):
            sum += i
            if(num / i != i):
                sum += num / i
    return int(sum)

def getSumOfNonAbundantSums(arr, limit):
    nonAbundantSums = []
    for i in range(1, limit):
        nonAbundantSums.append(i)
    for i in range(0,len((arr))):
        for k in range(i,len(arr)):
            sumOfTwo = arr[i] + arr[k]
            if(sumOfTwo - 1 < len(nonAbundantSums)):
                nonAbundantSums[sumOfTwo - 1] = 0
    return addArr(nonAbundantSums)
def addArr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
def main():
    limit = 28123
    seconds = time.time()
    abundant = getAllAbundantNums(limit)
    final = getSumOfNonAbundantSums(abundant, limit)
    print(final)
    seconds2 = time.time()
    print(seconds2 - seconds, " seconds")

if(__name__ == "__main__"):
    main()
import math
import time
'''
    https://projecteuler.net/problem=23

    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

    Sets all sum of abundant numbers to 0 then adds the arr
'''
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
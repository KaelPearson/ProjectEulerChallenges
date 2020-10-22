'''
    https://projecteuler.net/problem=35

    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
'''
import time
import math
from collections import deque
def getAllRotations(number):
    num = []
    for i in str(number):
        num.append(int(i))
    arr = []
    for i in range(len(num)):
        arr.append(num[i:] + num[:i])
    newArr = []
    for i in arr:
        hold = ""
        for k in i:
            hold += str(k)
        newArr.append(int(hold))
    return newArr
def getListOfPrimes(limit):
    primes = []
    for i in range(2,limit+1):
        primes.append(i)
    count = 2
    actualPrimes = []
    while(count < math.sqrt(limit) + 1):
        for i in range(count - 1, len(primes)):
            if(primes[i] % count == 0):
                primes[i] = 0
                break
        count += 1
    return actualPrimes
def main():
    startTime = time.time()
    print(getListOfPrimes(100000))
    endTime = time.time()
    print(endTime - startTime, " Seconds Taken")
if(__name__ == "__main__"):
    main()
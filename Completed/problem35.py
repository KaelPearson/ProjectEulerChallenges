'''
    https://projecteuler.net/problem=35

    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?

    Takes two mins might come back to optimize
'''
import time
import math
def getRotations(num):
    arr = []
    numArr = [int(i) for i in str(num)]
    for i in range(len(numArr)):
        arr.append(numArr[i:] + numArr[:i])
    return arr
def getAllPrimesUnder(num):
    numList = [int(i) for i in range(2,num+1)]
    for i in range(2,int(math.sqrt(num) + 1)):
        for k in range(i-1, len(numList)):
            if(numList[k] % i == 0):
                numList[k] = 0
    return numList
# 0 means not prime shifted --> 2
def checkCircularPrime(primeList):
    possPrimeCircle = []
    for i in primeList:
        if(checkIfPoss(i) == True and i != 0):
            possPrimeCircle.append(i)
        else:
            possPrimeCircle.append(0)
    for i in possPrimeCircle:
        if(i != 0):
            rotations = getRotations(i)
            for k in rotations:
                num = ""
                for j in range(0, len(k)):
                    num += str(k[j])
                num = int(num)
                if(0 == possPrimeCircle[num - 2]):
                    possPrimeCircle[i - 2] = 0
    newArr = []
    for i in possPrimeCircle:
        if(i != 0):
            newArr.append(i)
    return newArr
def checkIfPoss(num):
    if(num == 5 or num == 2):
        return True
    for i in str(num):
        if(int(i) % 2 == 0 or int(i) == 5):
            return False
    return True
def main():
    startTime = time.time()
    primesUnder = getAllPrimesUnder(1000000)
    print(len(checkCircularPrime(primesUnder)))
    print(time.time() - startTime, " Seconds Taken")

if(__name__ == "__main__"):
    main()
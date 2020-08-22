import time
import math

def quadratic(n,a,b):
    ans = pow(n,2) + (a * n) + b
    return ans
def getAmountOfPrimes(a,b):
    n = 0
    while(checkPrime(quadratic(n,a,b)) == True):
        n += 1
    return n
def getAllNumbersInArr(limit):
    arr = [0]
    for i in range(1,limit):
        arr.append(i)
        arr.append(-i)
    return arr
primeList = [2]
def sieve(limit):
    arr = []
    for i in range(2,limit+1):
        arr.append(i)
    newArr = []
    for i in range(0,len(arr)):
        for k in range(2,int(math.sqrt(i) + 2)):
            if(arr[i] % k == 0):
                arr[i] = 0
    for i in range(0,len(arr)):
        if(arr[i] != 0):
            newArr.append(arr[i])
    return newArr
def checkPrime(num):
    num = abs(num)
    for i in primeList:
        if(i == num):
            return True
    for i in range(primeList[len(primeList) - 1], int(math.sqrt(num) + 1)):
        if(num % i == 0):
            return False
    return True
def checkAll(aArr, bArr):
    highest = 0
    for i in aArr:
        for k in bArr:
            amount = getAmountOfPrimes(i,k)
            if(amount > highest):
                highest = amount
                a = i
                b = k
    print(a*b)
    return "highest ", highest, " a ", a, " b ", b
def main():
    startTime = time.time()
    primeList = sieve(10000)
    bArr = sieve(1000)
    aArr = getAllNumbersInArr(1000)
    print(checkAll(aArr,bArr))
    endTime = time.time()
    print(endTime - startTime, " Seconds taken")
if(__name__ == "__main__"):
    main()
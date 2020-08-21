'''
    https://projecteuler.net/problem=27
'''
import time
import math
# get all prime for b
primeArr = []
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
            newArr.append(-arr[i])
    return newArr
# get 0 - 1 less than limit for a
def getAllNumbersInArr(limit):
    arr = []
    for i in range(0,limit):
        arr.append(i)
        arr.append(-i)
    return arr
def calculate(n, a, b):
    answer = pow(n,2) + a*n + b
    return answer
def solve(a,b):
    arr = []
    for i in range(0,abs(a)):
        arr.append(calculate(i,a,b))
    return arr
def checkArrPrime(arr):
    for i in arr:
        if(i > 0):
            for k in range(2,int(math.sqrt(i) + 2)):
                if(i % k == 0 and i != k):
                    return False
    return True
def checkAll(aArr, bArr):
    highest = 0
    pro = 0
    for i in bArr:
        for k in aArr:
            solu = solve(i,k)
            if(checkArrPrime(solu) == True):
                if(len(solu) > highest):
                    highest = len(solu)
                    pro = i * k
                    print(pro, " i ", i, " k ",k)
    return pro
def main():
    startTime = time.time()
    limit = 150
    bArr = sieve(limit)
    aArr = getAllNumbersInArr(limit)
    print(checkAll(aArr,bArr))

    endTime = time.time()
    print(endTime - startTime, " Seconds taken")

if(__name__ == "__main__"):
    main()
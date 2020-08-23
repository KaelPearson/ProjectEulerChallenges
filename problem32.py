'''
    https://projecteuler.net/problem=32

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

    1, 9, 1234, 9876
    12, 98, 123, 987
'''
import time
import math
# Returns True if arr is a 1-9 pandigital
def check(num1,num2,num3):
    arr = []
    for i in str(num1):
        arr.append(int(i))
    for i in str(num2):
        arr.append(int(i))
    for i in str(num3):
        arr.append(int(i))
    if(len(arr) != 9):
        return False
    arr.sort()
    for i in range(1,len(arr)):
        if(arr[i-1] != i):
            return False
    return True
arr1 = []
def checkAllInBounds(nStart, nEnd, n2Start, n2End):
    for i in range(nStart, nEnd + 1):
        for k in range(n2Start, n2End + 1):
            if(check(i,k,i*k) == True):
                arr1.append(i*k)
    return arr1
def totalNonDupes(arr):
    sum = 0
    newArr = []
    for i in range(0,len(arr) - 1):
        if(arr[i] != arr[i+1]):
            newArr.append(arr[i])
    newArr.append(arr[len(arr) - 1])
    print(arr)
    print(newArr)
    for i in newArr:
        sum += i
    return sum
def main():
    startTime = time.time()
    checkAllInBounds(1, 9, 1234, 9876)
    checkAllInBounds(12, 98, 123, 987)
    arr1.sort()
    print(totalNonDupes(arr1))
    endTime = time.time()
    print(endTime - startTime, " Seconds Taken")
if(__name__ == "__main__"):
    main()
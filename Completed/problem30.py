'''
    https://projecteuler.net/problem=30

    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import time
import math
def addArr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
def checkDigitPower(num, power):
    numbers = []
    for i in str(num):
        numbers.append(int(i))
    for i in range(0,len(numbers)):
        numbers[i] = pow(numbers[i], power)
    sum = addArr(numbers)
    if(sum == num):
        return True
    return False
def digitPowers(power):
    leng = pow(10,power + 1)
    arr = []
    for i in range(2,leng):
        if(checkDigitPower(i,power) == True):
            arr.append(i)
    sum = addArr(arr)
    return sum
def main():
    startTime = time.time()
    print(digitPowers(5))
    endTime = time.time()
    print(endTime - startTime, " Seconds taken")

if(__name__ == "__main__"):
    main()
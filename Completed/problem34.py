'''
    https://projecteuler.net/problem=34

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: As 1! = 1 and 2! = 2 are not sums they are not included.

    9! * 7 == 2540160 therefor the upper limit
'''
import time
import math


def getSumFactorialOfDigits(num):
    sum = 0
    for i in str(num):
        sum += math.factorial(int(i))
    return sum
def checkIfSumIsNum(num):
    sum = getSumFactorialOfDigits(num)
    if(sum == num):
        return True
    return False
def main():
    startTime = time.time()
    sum = 0
    for i in range(10,2540160):
        if(checkIfSumIsNum(i) == True):
            sum += i
    print(sum)
    endTime = time.time()
    print(endTime - startTime, " Seconds taken")

if(__name__ == "__main__"):
    main()
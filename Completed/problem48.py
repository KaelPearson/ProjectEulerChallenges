'''
    https://projecteuler.net/problem=48

    The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

    Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

    Just take the last 10 digits
'''
import time
import math
def getSumOfAllPrimeOfNumber(limit):
    sum = 0
    for i in range(0,limit+1):
        sum += pow(i,i)
    return sum - 1
def main():
    print(getSumOfAllPrimeOfNumber(1000))
if(__name__ == "__main__"):
    main()
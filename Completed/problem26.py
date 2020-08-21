import time
import math
'''
    https://projecteuler.net/problem=26

    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

    This solution is very scuffed however it works
'''

def getLengthOfRepeating(num):
    length = 1
    nines = 9
    while(nines % num != 0):
        nines = nines * 10 + 9
        length += 1
        if(length == 1000):
            return -1
    return length
def main():
    startTime = time.time()
    highest = 0
    highestLen = 0
    for i in range(1,1001):
        if(getLengthOfRepeating(i) > highestLen):
            highest = i
            highestLen = getLengthOfRepeating(i)
    print(highest)
    endTime = time.time()
    print(endTime - startTime, " Seconds Taken")

if(__name__ == "__main__"):
    main()
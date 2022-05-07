"""
    Very bad solution that doesnt work lol
"""
import time
import numpy as np
def main():
    start = time.time()

    getHighestPrimePandigital(9999999)

    print(time.time() - start)

def getHighestPrimePandigital(limit):
    for i in range(limit, 0, -1):
        if(checkPandigital(i)):
            if(checkPrime(i)):
                print(i)
                break

def checkPrime(num):
    count = 3
    while (count * count < num):
        if(num % count == 0):
            return False
        count += 1
    return True
def checkPandigital(num):
    arr = [0] * 9
    for char in str(num):
        arr[int(char) - 1] += 1
    for i in arr:
        if(i != 1):
            return False
    return True
if(__name__ == "__main__"):
    main()
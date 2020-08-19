import math
import time

arr = []
'''
    50 1
    
'''
a = 1
b = 2
c = 3
d = 4

def poss(limit):
    startingNum = []
    for i in range(0,limit):
        startingNum.append(1)
    while(startingNum[0] < 5):
        if(startingNum[0] == 4):
            return startingNum
        if(startingNum[0] == 1):
            startingNum.pop(0)
            startingNum[(len(startingNum) - 1)] += 1
        
        
    return startingNum

def main():
    print(poss(5))

if(__name__ == "__main__"):
    main()
'''

'''
import time
import math
valuesToCheck = [1,2,5,10,20,50,100,200]
def count(n):  
    table = [0 for i in range(n+1)] 
    table[0] = 1
    for i in valuesToCheck:
        table = addValue(i,n,table)
    return table[n]
def addValue(num,n,table):
    for i in range(num, n+1):
        table[i] += table[i-num]
    return table
def main():
    startTime = time.time()
    print(count(200))
    endTime = time.time()
    print(endTime - startTime, " Seconds taken")

if(__name__ == "__main__"):
    main()
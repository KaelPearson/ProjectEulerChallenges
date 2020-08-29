'''

'''
import time
import math

def checkCancel(num, deno):
    arr = []
    for i in str(num):
        arr.append(i)
    for i in str(deno):
        for k in range(0,len(arr)):
            if(i == arr[k]):
                return int(i)
    return False
def checkDec(num, deno):
    oldDec = num / deno
    cancel = checkCancel(num, deno)
    if(cancel == False):
        return False
    for i in str(num):
        if(int(i) != cancel):
            num = int(i)
    for i in str(deno):
        if(int(i) != cancel):
            deno = int(i)
    if(len(str(num)) == 2):
        deno = cancel
        num = cancel
    if(deno == 0):
        return False
    newDec = num / deno
    #print(oldDec, " oldDec")
    #print(newDec, " newDec")
    if(oldDec == newDec):
        return True
    return False
def checkAll():
    arrNum = []
    arrDeno = []
    for i in range(10,100):
        for k in range(10, i):
            if(checkDec(k,i)):
                arrNum.append(k)
                arrDeno.append(i)
    print(arrNum)
    print(arrDeno)
    sum = 0.0
    for i in range(0,len(arrNum)):
        sum += arrNum[i] / arrDeno[i]
    return sum
def main():
    startTime = time.time()
    print(checkAll())
    endTime = time.time()
    print(endTime - startTime, " Seconds taken")

if(__name__ == "__main__"):
    main()
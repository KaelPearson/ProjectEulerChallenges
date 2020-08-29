'''
    https://projecteuler.net/problem=33

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
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
    prodOfDeno = 1
    for i in arrDeno:
        prodOfDeno *= i
    prodOfNum = 1
    for i in arrNum:
        prodOfNum *= i
    return prodOfDeno / prodOfNum
def main():
    startTime = time.time()
    print(checkAll())
    endTime = time.time()
    print(endTime - startTime, " Seconds taken")

if(__name__ == "__main__"):
    main()
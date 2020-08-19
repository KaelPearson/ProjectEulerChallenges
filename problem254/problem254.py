'''
    https://projecteuler.net/problem=254
    Define f(n) as the sum of the factorials of the digits of n. For example, f(342) = 3! + 4! + 2! = 32.

    Define sf(n) as the sum of the digits of f(n). So sf(342) = 3 + 2 = 5.

    Define g(i) to be the smallest positive integer n such that sf(n) = i. Though sf(342) is 5, sf(25) is also 5, and it can be verified that g(5) is 25.

    Define sg(i) as the sum of the digits of g(i). So sg(5) = 2 + 5 = 7.

    Further, it can be verified that g(20) is 267 and ∑ sg(i) for 1 ≤ i ≤ 20 is 156.

    What is ∑ sg(i) for 1 ≤ i ≤ 150?


'''

'''
def getFacotorialDigits(num):
    sum = 0
    for i in num:
        currFac = 1
        for k in range(2,int(i) + 1):
            currFac *= k
        sum += currFac
    return str(sum)
def getSumOfDigits(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

def getSmallestSumOfDigits(num):
    currNum = 1
    while(True):
        if(getSumOfDigits(getFacotorialDigits(str(currNum))) == num):
            return str(currNum)
        currNum += 1
def getSG(num):
    return getSumOfDigits(num)

def getSGFor(start,limit):
    sum = 0
    for i in range(start,limit + 1):
        sum += getSG(getSmallestSumOfDigits(i))
    return sum
'''


'''
def getFac(num):
    total = 1
    for i in range(2,num + 1):
        total *= i
    return total

def getBiggestFac(num):
    biggest = 0
    for i in range(1,num + 1):
        if(getFac(i) >= num + 1):
            break
        biggest = i
    return biggest
def findAllBiggestFac(num):
    facs = []
    while(num >= 1):
        biggestFac = getBiggestFac(num)
        facs.append(biggestFac)
        num -= getFac(biggestFac)
    facs.sort()
    return facs
'''
'''
def getSumOfDigits(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum
'''
gList = [[]]
def getFacotorialDigits(num):
    sum = 0
    for i in num:
        currFac = 1
        for k in range(2,int(i) + 1):
            currFac *= k
        sum += currFac
    return str(sum)
def getSumOfDigits(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

# NOTE: This is G(i)
def getSmallestSumOfDigits(num):
    for i in range(0,len(gList) - 1):
        print(gList[1][i])
        #if(gList[1][i] == num):
        #    return str(gList[0][i])
    currNum = len(gList) + 1
    while(True):
        a = getSumOfDigits(getFacotorialDigits(str(currNum)))
        gList[0].append(currNum)
        gList[1].append(a)
        if(a == num):
            return str(currNum)
        currNum += 1
def getSG(num):
    return getSumOfDigits(num)

def getSGFor(start,limit):
    sum = 0
    for i in range(start,limit + 1):
        sum += getSG(getSmallestSumOfDigits(i))
    return sum
def main():
    print(getSGFor(1,2))

if(__name__ == "__main__"):
    main()
# both sg and sf use this
def getSumOfDigits(num):
    sumOfDigits = 0
    for i in str(num):
        sumOfDigits += int(i)
    return sumOfDigits
# f
def getSumOfFactorialDigits(num):
    total = 0
    for i in str(num):
        factorialOfDigits = 1
        for k in range(2,int(i) + 1):
            factorialOfDigits *= k
        total += factorialOfDigits
    return total

def getf(num):
    return getSumOfFactorialDigits(num)
def getsf(num):
    return getSumOfDigits(getSumOfFactorialDigits(num))
def getsg(num):
    return getSumOfDigits(getsf(num))
def getAllsg(amount):
    allsg = []
    for i in range(1,amount + 1):
        allsg.append(-1)
    count = 1
    while(True):
        currentsg = getsg(count)
        if(currentsg <= amount):
            if(allsg[currentsg-1] == -1):
                allsg[currentsg - 1] = count

        count += 1
        for i in range(0,amount):
            if(allsg[i] == -1):
                break
            elif(i == (amount - 1)):
                return allsg
def addArr(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum += arr[i]
    return sum
def main():
    print(getAllsg(15))

if(__name__ == "__main__"):
    main()
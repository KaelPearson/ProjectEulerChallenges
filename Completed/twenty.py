numToFac = 100

def getStrFac(num):
    sum = 1
    for i in range(1, num+1):
        sum *= i
    return str(sum)

def getTotalDigits(string):
    sum = 0
    for i in string:
        sum += int(i)
    return sum

def main():
    print(getTotalDigits(getStrFac(numToFac)))

if __name__ == "__main__":
    main()
'''
    https://projecteuler.net/problem=20
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

    Big numbers
'''

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
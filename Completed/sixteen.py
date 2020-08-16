# Switched from js to python bc of very large numbers
'''
    https://projecteuler.net/problem=16
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    just pow of number to pow then add digits
'''
number = 2
power = 1000


def main():
    numberPow = pow(number,power)
    sum = 0
    numberPow = str(numberPow)
    for i in numberPow:
        sum += int(i)
    print(sum)

if __name__ == "__main__":
    main()
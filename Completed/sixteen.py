
# Switched from js to python bc of very large numbers

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
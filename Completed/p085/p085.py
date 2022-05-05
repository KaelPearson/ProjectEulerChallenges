import math


def main():
    value = 2000000
    close = 0
    m = 0
    n = 0
    for i in range(1, 3000):
        for k in range(1,3000):
            rect = int(numberOfRect(i,k))
            if(abs(rect - value) < abs(close - value)): 
                close = rect
                m = i
                n = k
    print(str(m) + " " + str(n))
    print(numberOfRect(36,77))




def numberOfRect(m, n):
    num1 = ((m + 1) * m) / 2
    num2 = ((n + 1) * n) / 2
    return num1 * num2
if __name__ == "__main__":
    main()
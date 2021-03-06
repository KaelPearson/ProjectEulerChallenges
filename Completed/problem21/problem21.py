'''
    https://projecteuler.net/problem=21
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

    
'''


# p = (2^(n-m) + 1) * 2^m - 1
# q = (2^(n-m) + 1) * 2^n - 1
# r = (2^(n-m) + 1)^2 * 2^(m+n) - 1

# n > m > 0
# if pqr are prime 
    # then 2^n * p * q and 2^n * r are pair of amicable numbers



# Eulers Rule doesnt work for this
# I programmed this thinking it did
# Going to come back and switch to a method to check divisors of each number 
# Cant think other than to brute force with some useful efficent additions

import math

def checkPrime(num):
    for i in range(2,int(math.sqrt(num)) + 1):
        if(num % i == 0):
            return False
    return True
def main():
    p = 0
    q = 0
    r = 0

    n = 2
    m = 1
    while n < 10:
        if(m + 1 == n):
            n += 1
            m = 1
        else:
            m += 1
        p = (pow(2,(n-m)) + 1) * pow(2,m) - 1
        if(checkPrime(p)):
            q = (pow(2,(n-m)) + 1) * pow(2,n) - 1
            if(checkPrime(q)):
                r = pow((pow(2,(n-m)) + 1), 2) * pow(2,(m+n)) - 1
                if(checkPrime(r)):
                    print("p ", p, " q ", q, " r ", r)
                    print("1 ", (pow(2,n) * p * q))
                    print("2 ", (pow(2,n) * r))

if(__name__ == "__main__"):
    main()

"""

"""
import numpy as np
def main():
    print(champernowneConstant(10))

def champernowneConstant(max):
    sum = 0
    kSum = 0
    for i in range(1,max):

        for k in range(1,i):
            kSum += np.log10(k+1)
        sum += i / (10 * kSum)
        kSum = 0
    return sum
if(__name__ == "__main__"):
    main()
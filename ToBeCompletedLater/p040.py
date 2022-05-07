"""
    Cant figure out how to est that far out will come back
"""
import time
def main():
    start = time.time()
    print(champernowneConstant())
    print(time.time() - start)

def champernowneConstant():
    constant = 0.123456789
    mul = pow(10,-9)
    div = 991 / 9801
    return ('%.80f' % (constant + mul  * div))

if(__name__ == "__main__"):
    main()
"""
Problem 39 https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import time
def main():
    start = time.time()
    max = 0
    value = None
    for i in range(1,1001):
        solu = getSolu(i)
        if(max < solu):
            max = solu
            value = i
    print(max)
    print(value)
    # Print time
    print(time.time() - start)

def getSolu(num):
    solutions = []
    for i in range(int(num/3), int(num/2)):
        c = i
        for k in range(1, int(num/3)):
            a = k
            b = num - c - a
            if(checkTri(a,b,c)):
                solutions.append([a,b,c])
                break
    return len(solutions)
"""
Works but inefficent
def getSolu(num):
    solutions = []
    for i in range(1, int(num / 3)):
        for k in range(1, int(num - i)):
            a = i
            b = k
            # Make sure adds up
            c = num - a - b
            if(checkTri(a,b,c)):
                solutions.append([a,b,c])
    return len(solutions)
"""     

def checkTri(a,b,c):
    a2 = pow(a,2)
    b2 = pow(b,2)
    c2 = pow(c,2)
    if(a2 + b2 == c2):
        return True
    return False



if(__name__ == "__main__"):
    main()
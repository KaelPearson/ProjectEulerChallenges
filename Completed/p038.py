"""
    Problem 038 https://projecteuler.net/problem=38

    *** SUPER sloppy maybe will choose to improve in the future but we all know thats a lie ;) ***
    

    Take the number 192 and multiply it by each of 1, 2, and 3:

        192 × 1 = 192
        192 × 2 = 384
        192 × 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""
import time
def main():
    start = time.time()
    biggest = 5000000 # 1 000 000 000 / 2 == biggest pos value
    smallest = 1
    n = 2
    max = 0
    
    for k in range(0,5):
        for i in range(biggest,smallest,-1):
            num = getNString(i,n)
            
            # From largest to smallest if pandigital step up n and move on
            if(checkPandigital(num) == True):
                if(num > max):
                    max = num
                    smallest = max
                break
        n += 1

    print(max)
    end = time.time()
    print("Seconds: " + str(end - start))

# Recursive call for getting N String returns int
def getNString(num, n):
    if(n == 0):
        return ""
    return int(str(getNString(num, n-1)) + str(num * n))

# Checks if number is 1-9 pandigital with a max of 1 in each number
def checkPandigital(num):
    stringNum = str(num)
    if(len(stringNum) != 9):
        return False
    arr = [0] * 9
    for char in stringNum:
        arr[int(char) - 1] += 1
    for i in arr:
        if(i != 1):
            return False
    return True
if (__name__ == "__main__"):
    main()
'''
    https://projecteuler.net/problem=24

    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import time
import itertools
nums = [0,1,2,3,4,5,6,7,8,9]
def getAllCombinations(arr):
    combinations = []
    num = 0
    for value in itertools.permutations(arr, 10):
        num += 1
        if(num == 1000000):
            return value
        
def main():
    startTime = time.time()
    print(getAllCombinations(nums))
    endTime = time.time()
    print(endTime - startTime, " seconds taken")

if(__name__ == "__main__"):
    main()
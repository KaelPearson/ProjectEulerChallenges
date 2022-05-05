import numpy as np


def main():
    max = 0
    maxValueExp = 0
    valueExp = getValueExpArr() # [n][0] = value      [n][1] = Exp
    for i in valueExp:
        totalValue = getTotalValue(i) # x^y == y * ln(x)
        if(totalValue > max):
            max = totalValue
            maxValueExp = i
    print(maxValueExp) # Highest combo
    print(valueExp.index(maxValueExp) + 1) # Index


"""
    x^y == y * ln(x)
"""
def getTotalValue(valueExp):
    x = valueExp[0]
    y = valueExp[1]
    return y * np.log(x)


"""
    getValueExpArr() = get Value and Exp in 2d array with first value at [n][0] being value and [n][1] being exp
    Stored as int values within 2d array
"""
def getValueExpArr():
    textarr = []
    file = open("p099_base_exp.txt", "r")
    for i in file.readlines():
        textarr.append(i)
    file.close()
    valueExp = []
    for i in textarr:
        # Remove \n
        i = i.strip()
        # Seperate values by ,
        i = i.split(",")

        # Add them so they can be put in 2d array
        both = []
        both.append(int(i[0]))
        both.append(int(i[1]))
        
        # append
        valueExp.append(both)
    return valueExp
"""
    Test for correct value typing + working correctly
"""
def testGetValueExpArr(valueExp):
    print("\n-----\n")
    print("TESTING getValueExpArr\n")
    # Test first 5 values
    for i in range(0,5):
        print(valueExp[i]) # print first 5 base and exp
        print(valueExp[i][0] + valueExp[i][1]) # Add base and exp
    res = isinstance(valueExp[i][0], int)
    print("Stored as ints: " + str(res))

    print("\nEND TESTING getValueExpArr")
    print("\n-----\n")
    
    
if __name__ == "__main__":
    main()

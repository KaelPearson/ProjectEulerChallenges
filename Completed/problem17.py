'''
    https://projecteuler.net/problem=17
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

    Probably one of the most painful ones but just figured out how many times each parts occurs then added them together
'''
tens = ["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]

ones = ["one","two","three","four","five","six","seven","eight","nine"]

end = 1000

def main():
    sum = 0
    """
    for i in range(1,end):
        strI = str(i)
        if(len(strI) == 1):
            sum += len(ones[i - 1])
        elif(len(strI) == 2):
            sum += len(tens[int(strI[0]) - 1])
            if(strI[1] != 0):
                sum += len(ones[int(strI[1]) - 1])
        elif(len(strI) == 3):
            sum += len(ones[int(strI[0]) - 1])
            if(strI[1] != 0):
                sum += len(tens[int(strI[1]) - 1])
            if(strI[2] != 0):
                sum += len(ones[int(strI[2]) - 1])
            if(strI[1] == 0 and strI[2] == 0):
                sum += len("hundred")
            else:
                print("there")
                sum += len("hundredand")
        elif(len(strI) == 4):
            sum += len("onethousand") 
    """
    onesTotal = 0
    tensTotal = 0
    for i in range(0,9):
        onesTotal += len(ones[i])
    oneToNinetyNine = onesTotal + 10*(46) + 8 * 36  + 70
    print(oneToNinetyNine)
    sum += onesTotal*100 # 3600
    print(onesTotal*100)
    sum += oneToNinetyNine*9 # 7686
    print(oneToNinetyNine*9)
    sum += 7*9 # hundreds 63
    print(7*9)
    sum += 10*891 # hundredsand 8910
    print(10*891)
    print(sum + oneToNinetyNine + 11)

if __name__ == "__main__":
    main()
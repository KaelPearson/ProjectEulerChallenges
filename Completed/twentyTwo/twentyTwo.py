'''
    https://projecteuler.net/problem=22
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?

    Changed names.txt to array format
'''

def main():
    file = open("names.txt", "r")
    names = file.read().split(',')
    file.close
    for i in range(0,len(names)):
        names[i] = names[i].replace('"', '')
    names = sorted(names)
    sum = 0
    for i in range(0,len(names)):
        nameSum = 0
        for k in names[i]:
            nameSum += ord(k) - 64
        nameSum *= i + 1
        sum += nameSum
    print(sum)

    

if(__name__ == "__main__"):
    main()
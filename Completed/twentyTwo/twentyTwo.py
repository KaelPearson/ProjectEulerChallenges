

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
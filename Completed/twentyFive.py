

def main():
    fib1 = 1
    fib2 = 1
    count = 3
    while(len(str(fib1 + fib2)) < 1000):
        oldFib1 = fib1
        fib1 = fib2
        fib2 = oldFib1 + fib2
        count+=1
    print(count)

if(__name__ == "__main__"):
    main()
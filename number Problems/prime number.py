n = int(input("Enter the number: "))

if n <= 1: print(False)
elif n == 2: print(True)
elif n % 2 == 0: print(False)
else:
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            print(False)
    print(True)




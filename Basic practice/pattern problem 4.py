n = int(input("Enter a number: "))

for i in range(1,n+1):
    print(" " * (n-i),"* " * i)
    if i == n:
        for j in range(1, n):
            print(" " * j, "* " * (n - j))
n = 5
print("below is problem 1")
for i in range(1, n + 1):
    print(i)    # same, default print syntax -> print(i, end="\n")

print("below is problem 2")
for i in range(1, n + 1):
    print(i, end=" ") # print generally end with \n but here I gave a condition that it should end with space


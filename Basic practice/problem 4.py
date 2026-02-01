n = 5
'''
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
temp = 0
for i in range(1, n + 1):
    temp = (temp * 10) + i
    print(temp)

n = 5
''' solution1
for i in range(1, n + 1):
    for j in range(1, n +1):
        print(j, end=" ")
    n -=1
    print()

solution2
n = 5
while n > 0:
    for j in range(1, n + 1):
        print(j, end=" ")
    n -= 1
    print()
'''
'''
12345
1234
123
12
1
'''
temp = 0
# for j in range(1, n + 1):
m = n
for j in range(1, n + 1):
    temp = 0
    for i in range(1, m + 1):
        temp = temp + (i * (10 ** (m - i)))
    m = m-1
    print(temp)







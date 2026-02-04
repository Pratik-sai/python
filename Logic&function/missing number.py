# consecutive number total formula for 1,2...n = (n*(n+1))/2

num = [1, 2, 3, 4, 5, 7, 8, 9, 10]
#print(sum(num))

last_num = num[-1]
print(last_num)
missing_num = ((last_num * (last_num + 1)) // 2) - sum(num)
print(missing_num)

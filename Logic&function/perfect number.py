n = int(input("Enter a number: "))

tot_sum = 0
list1 = []
for i in range(1, (n//2)+1):
    if n % i == 0:
        list1.append(i)
        tot_sum += i
print(list1)
print(tot_sum == n)
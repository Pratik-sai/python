#methtod 1
def lar_num(n):
    return max(n)
n = input("values are ").split()
print(lar_num(n))

#method 2
max_num = n[0]
for i in range(len(n)):
    if int(n[i]) > int(max_num):
        max_num = n[i]
print(f"largest number is {max_num}")


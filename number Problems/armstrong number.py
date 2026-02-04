n = int(input("Enter a number: "))

num_len = len(str(n))
armstrong_num = 0

for i in range(num_len):
    armstrong_num = armstrong_num + (int(str(n)[i]) ** num_len)

print(armstrong_num == n)

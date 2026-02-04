list1 = [23, 56, 12, 19, 46, 94]

### solution1
'''
print(f"largest num is {max(list1)}")
print(f"smallest num is {min(list1)}")
'''

### solution2
max_num = min_num = list1[0]

for i in range(len(list1)):
    if list1[i] > max_num:
        max_num = list1[i]
    elif list1[i] < min_num:
        min_num = list1[i]

print(f"largest num is {max_num}")
print(f"smallest num is {min_num}")


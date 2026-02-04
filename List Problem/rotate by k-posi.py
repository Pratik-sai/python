list1 = [1,2,3,4,5]
position = 2

list2 = list1[position:] + list1[:position]
print(list2)
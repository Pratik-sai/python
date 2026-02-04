str1 = "saipratiks"

for i in range(len(str1)):
    if str1[i] not in str1[i+1:]:
        print(str1[i])
        break


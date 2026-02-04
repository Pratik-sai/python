dict1 = {'a': 2, 'i': 2, 's': 1, 'p': 1, 'r': 1, 't': 1, 'k': 1}
dict2 = {'b' : 1, 'e' : 2, 'r' : 1, 'a' : 1}
### solution 1
print(dict1 | dict2)

### solution 2
dict1.update(dict2)
print(dict1)
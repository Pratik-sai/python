str1 = input("Enter a string: ")

vowels = ['a', 'e', 'i', 'o', 'u']

vowels_count = 0
consonant_count = 0

for i in str1:
    if i in vowels:
        vowels_count += 1
    else:
        consonant_count += 1

print(f"Number of vowels: {vowels_count}")
print(f"Number of consonants: {consonant_count}")
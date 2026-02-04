word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

if sorted(word1) == sorted(word2):
    print("Both words are anagrams")
else:
    print("One word is not anagrams")
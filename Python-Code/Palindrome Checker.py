word = input('Please give me a word to check if its palindrome: ')
backwards = word[::-1]
backwards = backwards.lower()
if backwards == word.lower():
    print( word + ' is a palindrome!')
else:
    print( word + ' is not a palindrome.')
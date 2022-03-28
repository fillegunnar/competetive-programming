from math import factorial

word = input()
letters = {}
for letter in word:
    if letter not in letters.keys():
        letters[letter] = 1
    else:
        letters[letter] += 1

perm = factorial(len(word))
for letter in letters.keys():
    perm //= factorial(letters[letter])

print(perm)
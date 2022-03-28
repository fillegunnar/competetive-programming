import sys

n = int(input())
anagram_groups = {}
seq = sys.stdin.read().split()

for i in range(n):
    word = seq[i]
    sorted_word = "".join(sorted(word))
    if sorted_word in anagram_groups.keys():
        anagram_groups[sorted_word].append(word)
    else:
        anagram_groups[sorted_word] = [word]

for key in list(anagram_groups.keys()):
    if len(anagram_groups[key]) < 2:
        del anagram_groups[key]

print(len(anagram_groups))
for key in anagram_groups.keys():
    print(len(anagram_groups[key]))
    for word in anagram_groups[key]:
        print(word)
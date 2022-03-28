# dict_size = int(input())
# dictionary = []
# length_of_words_in_dict = []
# anagram_groups = []

# for i in range(dict_size):
#     temp = input()
#     dictionary.append(temp[:-1])
#     length_of_words_in_dict.append(len(temp))

# # Search for anagrams
# for i in range(dict_size):
#     word1 = dictionary[i]
#     word_already_handled = False
#     for group in anagram_groups:
#         if word1 in group:
#             word_already_handled = True
#     if word_already_handled:
#         continue
#     current_anagram_group = []
#     current_anagram_group.append(word1)
#     for j in range(i+1, dict_size):
#         word2 = dictionary[j]
#         if len(word1) != len(word2):
#             continue
#         # If were here they are the same length
#         anagram = True
#         for letter in word1:
#             if letter not in word2:
#                 anagram = False
#                 break
#         if anagram:
#             current_anagram_group.append(word2)
    
#     if len(current_anagram_group) > 1:
#         anagram_groups.append(current_anagram_group)
    
# # Done with search, print anagrams
# print(len(anagram_groups))
# for group in anagram_groups:
#     print(len(group))
#     for word in group:
#         print(word)

dict_size = int(input())
anagram_groups = {}

for i in range(dict_size):
    word = input()
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
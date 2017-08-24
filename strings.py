import string
import re

# Uppercase a string
# my_string = "this is my string"
# print(my_string).upper()


# Capatalize a string
# my_string = "this is my string"
# print(my_string).capitalize()


# Reverse a string
# my_string = "this is my string"[::-1]
# print(my_string)

# Leetspeak
# replacements = ( ('A','4'), ('E','3'), ('G','6'), ('I','1'),
#                  ('O','0'), ('S','5'), ('T','7') )
# my_string = "Leet is too neat"
# new_string = my_string.upper()
# for old, new in replacements:
#     new_string = new_string.replace(old, new)
#
# print(new_string)


# Long Long Vowels
# word = raw_input("Enter a word containing long vowels: ")
# word = word.replace('aa', 'aaaaa')
# word = word.replace('ee', 'eeeee')
# word = word.replace('ii', 'iiiii')
# word = word.replace('oo', 'ooooo')
# word = word.replace('uu', 'uuuuu')
# print(word)

# # print(re.sub("a|e|i|o|u", "oo", word))
# new_word = ""
# for ch in word:
#     if ch in "aa":
#            new_word = word.replace(ch,'aa')
#     elif ch in "ee":
#            new_word = word.replace(ch,'ee')
#     elif ch in "ii":
#            new_word = word.replace(ch,'ii')
#     elif ch in "oo":
#            new_word = word.replace(ch,'oo')
#     elif ch in "uu":
#            new_word = word.replace(ch,'uu')
# print(new_word)


# Caesar Cipher
# text = "lbh zhfg hayrnea jung lbh unir yrnearq"
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# k = 13
# answer = ''
# for c in text:
#     if c in alphabet:
#         answer += alphabet[(alphabet.index(c)+k)%(len(alphabet))]
# print(answer)

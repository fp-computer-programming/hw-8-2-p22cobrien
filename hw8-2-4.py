# Author: CMOB 12/7/2021

def letter_count(word, letter):
    total = str.count(word, letter)
    return total

print(letter_count("cat", "t") == 1)
print(letter_count("apple", "p") == 2)
print(letter_count("supercalifragilisticexpialidocious", "i") == 7)

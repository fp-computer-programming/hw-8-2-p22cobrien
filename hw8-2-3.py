# Author: CMOB 12/7/2021

def three_letter_words(word):
    total = 0
    for x in word:
        if len(x) <= 3:
            total += 1
    return total

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)

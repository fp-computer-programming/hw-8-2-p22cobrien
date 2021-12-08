# Author: CMOB 12/7/2021

def sum_odds(num):
    total = 0
    for x in num:
        if x % 2 != 0:
            total += x
        else:
            continue
    x += 1
    return total

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)

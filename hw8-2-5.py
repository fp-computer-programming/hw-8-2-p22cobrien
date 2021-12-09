# Author: CMOB 12/8/2021

def sum_no_odd(num):
    total = 0
    z = 0
    for x in num:
        if z < len(num):
            if x % 2 == 0:
                total += x
            elif x % 2 != 0:
                z += len(num)
    return total


print(sum_no_odd([2, 4, 6, 8, 9]) == 20)
print(sum_no_odd([13, 12, 10]) == 0)
print(sum_no_odd([14, 16, 32]) == 62)

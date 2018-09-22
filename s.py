from math import fabs

def number_needed(a, b):
    letterArray = [0] * 26
    for c in a:
        index = ord(c) - ord('a');
        letterArray[index] += 1
    for c in b:
        index = ord(c) - ord('a')
        letterArray[index] -= 1
    result = 0
    for i in letterArray:
        result += fabs(i)
    return int(result)


a = input().strip()
b = input().strip()

print(number_needed(a, b))

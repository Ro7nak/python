from math import fabs


def number_needed(a, b):
    letterArray = [0] * 26
    for c in a:
        index = (ord(c) - ord('a'))
        letterArray[index] += 1
    for c in b:
        index = ord(c) - ord('a')
        letterArray[index] -= 1
    result = 0
    for i in letterArray:
        result += fabs(i)
    print(int(result))


test = open("test.txt", "r")
x = []
for i in test:
    x.append(i)
#print(x)

for i in range(1,int(x[0])+1):
    a, b = x[i].split()
    number_needed(a, b)

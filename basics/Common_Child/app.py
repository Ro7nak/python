import math
import os
import random_app_demo
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    a = []
    b = []
    for i in s1:
        a.append(i)
    for i in s2:
        b.append(i)
    s = []
    # print(a)
    # print(b)
    for i in range(len(a)-1):
        for j in range(len(b)):
            if a[i] == b[i]:
                x = ""
                x += b[j]
                s.append(x)



    return s


test = open("test.txt", "r")
s = []

for i in test:
    s.append(i)

s1 = s[0]

s2 = s[1]

result = commonChild(s1, s2)

print(result)


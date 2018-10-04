# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    a = []
    b = []
    a1 = []
    count = 0
    for x in range(i,j+1):
        a.append(x)
    b = a.copy()
    print(b)
    for i in range(len(a)):
        reverse = 0
        while a[i] >0:
            n = a[i] % 10
            reverse = (reverse*10) + n
            a[i] = a[i] // 10
        a1.append(reverse)
    for i in range(len(a1)):
        if float(abs(b[i] - a1[i]) / k).is_integer():
            count += 1
    return count


'''
def beautifulDays(i, j, k):
    a = []
    count = 0
    for x in range(i,j+1):
        a.append(x)
    for i in range(len(a)):
        if float(abs(a[i] - int(str(a[i])[::-1])) / k).is_integer():
            count += 1
    return count
'''

ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
result = beautifulDays(i, j, k)
print(result)

'''
sample input:
20 23 6
'''
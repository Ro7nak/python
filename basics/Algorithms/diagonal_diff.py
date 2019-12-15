# https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random_app_demo
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    l = len(arr[0])
    a = 0
    b = 0
    for i in range(l):
        a += arr[i][l-1-i]
        b += arr[i][i]
    return abs(b-a)


n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)

'''
sample input:
3
11 2 4
4 5 6
10 8 -12
'''
# https://www.hackerrank.com/challenges/minimum-distances/problem

import math
import os
import random_app_demo
import re
import sys


# Complete the minimumDistances function below.
def minimumDistances(a):
    s = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                s.append(abs(i - j))

    if len(s) != 0:
        return min(s)
    else:
        return -1


n = int(input())
a = list(map(int, input().rstrip().split()))
result = minimumDistances(a)
print(result)

'''
sample input:
6
7 1 3 4 1 7
'''
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random_app_demo
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


test = open("test.txt", "r")
a = []
for i in test:
    a.append(i)
t = int(a[0])

for i in range(t):
    n = int(a[1 + (i * 2)])
    q = list(map(int, a[2 + (i * 2)].rstrip().split()))
    minimumBribes(q)

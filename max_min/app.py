<<<<<<< HEAD
import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    b = []
    unfairness = []
    a = list(map(int, arr))
    for i in combinations(arr, k):
        b.append(i)
    for i in b:
        unfairness.append(max(i) - min(i))
    #print(b)
    return min(unfairness)


test = open("test3.txt", "r")
a = []
for i in test:
    a.append(i)

n = int(a[0])

k = int(a[1])

arr = []

for i in range(n):
    arr_item = int(a[i+2])
    arr.append(arr_item)

result = maxMin(k, arr)

print(result)
=======
import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    b = []
    unfairness = []
    a = list(map(int, arr))
    for i in combinations(arr, k):
        b.append(i)
    for i in b:
        unfairness.append(max(i) - min(i))
    #print(b)
    return min(unfairness)


test = open("test3.txt", "r")
a = []
for i in test:
    a.append(i)

n = int(a[0])

k = int(a[1])

arr = []

for i in range(n):
    arr_item = int(a[i+2])
    arr.append(arr_item)

result = maxMin(k, arr)

print(result)
>>>>>>> 8287f82b3a8c4d2357374234cd6f52e4813e2603

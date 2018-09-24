import math
import os
import random
import re
import sys
from collections import Counter


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    sum = 0
    x = Counter(ar)
    # print(x.values())
    for i in x.values():
        if (i % 2) == 0:
            sum += int(i / 2)
        else:
            sum += math.floor(i / 2)
    return sum


test = open("test.txt", "r")
a = []
for i in test:
    a.append(i)
n = int(a[0])

ar = list(map(int, a[1].rstrip().split()))

result = sockMerchant(n, ar)

print(result)
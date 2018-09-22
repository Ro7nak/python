import math
import os
import random
import re
import sys
from collections import Counter

'''
Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

For example, if  and , we can delete  from string  and  from string  so that both remaining strings are  and  which are anagrams.
'''

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    x = []
    for i in a:
        x.append(i)
    y = []
    for i in b:
        y.append(i)
    count = 0
    x = sorted(x)
    y = sorted(y)
    len1 = len(x)
    len2 = len(y)
    if len(x) >= len(y):
        for i in range(len(y)):
            for j in range(len(x)):
                if y[i] == x[j]:
                    count += 1
                    x.remove(x[j])
                    break
    else:
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    count += 1
                    y.remove(y[j])
                    break
    return len1+len2-(count*2)


test = open("test.txt", "r")
z = []
for i in test:
    z.append(i)

for i in range(1, int(z[0])+1):
    x = z[i].split()
    res = makeAnagram(x[0], x[1])
    print(res)

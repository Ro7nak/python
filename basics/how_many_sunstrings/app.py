# https://www.hackerrank.com/challenges/how-many-substrings/problem

import os
import sys
from collections import Counter
#
# Complete the countSubstrings function below.
#
def countSubstrings(s, queries):
    temp = ""
    count = []
    for i in range(len(queries)):
        temp = s[queries[i][0]:queries[i][1]+1]
        if temp == temp[-1]:
            print(temp)
            count.append("1")
        else:
            z = []
            for i in range(len(temp)):  # will give all possible combination of substrings
                for j in range(i,len(temp)):
                    #print(temp[i:j+1])
                    z.append(temp[i:j+1])
            d = set(z)
            print(d)
            count.append(str(len(d)))
    return count


test = open("test.txt", "r")
a = []
for i in test:
    a.append(i)
nq = a[0].split()
n = int(nq[0])
q = int(nq[1])
s = a[1]
queries = []
print(s)
for i in range(q):
    queries.append(list(map(int, a[i+2].rstrip().split())))

result = countSubstrings(s, queries)
for i in result:
    print(i)

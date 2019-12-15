# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


'''
n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
max = x = 0
#print(list)
for i in list:
    x=x+i;
    if(max<x): max=x;
print(max)
'''


import math
import os
import random_app_demo
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0]*(n +1)
    z=[]
    for i in queries:
        z.append(i)
    # print(z[0][2])
    # print(a[int(z[0][0])]+int(z[0][2]))
    for i in range(len(z)):
        for j in range(int(z[i][0]),int( z[i][1])+1):
            a[j] = a[j]+int ( z[i][2])
    print(a)
    return max(a)


test = open("test.txt", "r")
a = []
for i in test:
    a.append(i)
nm = a[0].split()
n = int(nm[0])
m = int(nm[1])
queries = []
for i in range(1,m+1):
    queries.append(list(map(int, a[i].rstrip().split())))
result = arrayManipulation(n, queries)
print(result)

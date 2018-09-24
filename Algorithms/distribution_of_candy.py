'''
A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

For example, there are  prisoners and  pieces of candy. The prisoners arrange themselves in seats numbered  to . Let's suppose two is drawn from the hat. Prisoners receive candy at positions . The prisoner to be warned sits in chair number .

Function Description

Complete the saveThePrisoner function in the editor below. It should return an integer representing the chair number of the prisoner to warn.

saveThePrisoner has the following parameter(s):

n: an integer, the number of prisoners
m: an integer, the number of sweets
s: an integer, the chair number to begin passing out sweets from
'''

import math
import os
import random
import re
import sys


# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    a = [0] * n
    if n > m:
        for i in range(m):
            a[s + i] = 1
        for i in range(1,n-1):
            if a[-i] == 1:
                return len(a)-i
    else:
        m = (m % n)
        if s == n:
            for i in range(m):
                a[s-n+i] = 1
            for i in range(n):
                if a[-i] == 1:
                    return len(a)-i
        else:
            for i in range(m):
                a[s+i] = 1
        for i in range(1,n-1):
            if a[-i] == 1:
                return len(a)-i

t = int(input())
for t_itr in range(t):
    nms = input().split()

n = int(nms[0])
m = int(nms[1])
s = int(nms[2])
result = saveThePrisoner(n, m, s)
print(result)

'''
sample input 
2
7 19 2
3 7 3

2
5 2 1
5 2 2
'''

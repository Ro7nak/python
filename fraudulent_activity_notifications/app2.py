import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    a = []
    for i in range(0, d - 1):
        a.append(expenditure[i])

    for j in range(d, len(expenditure)):
        a.append(expenditure[j - 1])
        a.sort()
        median = 0
        if d % 2 == 0:
            x = int(d / 2)
            median = float((a[x - 1] + a[x]) / 2)
        else:
            median = a[len(a) // 2]
        if expenditure[j] >= 2 * median:
            count += 1
        # print(a)
        a.remove(expenditure[j - d])
    return count


'''
def activityNotifications(expenditure, d):
    count = 0
    a = []
    for i in range(0,d-1):
        a.append(expenditure[i])
    j = d
    while j < len(expenditure):
        a.append(expenditure[j-1])
        a.sort()
        median = 0
        if d%2 == 0:
            x= int(d/2)
            median = float((a[x-1]+a[x])/2)
        else:
            median = a[len(a) // 2]
        if expenditure[j] >= 2*median:
            count += 1
        a.remove(expenditure[j-d])
        j += 1
    return count
'''

test = open("test3.txt", "r")
a = []
for i in test:
    a.append(i)
nd = a[0].split()
n = int(nd[0])
d = int(nd[1])
expenditure = list(map(int, a[1].rstrip().split()))
result = activityNotifications(expenditure, d)
print(result)

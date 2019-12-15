# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

import math
import os
import random_app_demo
import re
import sys


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    for j in range(0, len(expenditure) - d):
        a = []
        for i in range(0 + j, d + j):
            a.append(expenditure[i])
        a.sort()
        median = 0
        if d % 2 == 0:
            x = int(d / 2)
            median = float((a[x - 1] + a[x]) / 2)
        else:
            median = a[len(a) // 2]
        if expenditure[d + j] >= 2 * median:
            count += 1
    return count


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

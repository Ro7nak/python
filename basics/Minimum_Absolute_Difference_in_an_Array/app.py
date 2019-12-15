import math
import os
import random_app_demo
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    '''
    arr = sorted(arr)
    diffs = []
    for i in range(len(arr)-1):
        ans = abs(arr[i]-arr[i+1])
        if ans==0:
            return ans
        else:
            diffs.append(ans)
    return min(diffs)
    '''

    '''
    a = []
    arr.sort()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            a.append(abs(arr[i] - arr[j]))

    a.sort()
    # print(a)
    # print("Length: " +str(len(a)))
    return a[0]
    '''
    arr.sort()
    temp = abs(arr[0] - arr[1])
    for i in range(len(arr) - 1):
        if (abs(arr[i] - arr[i+1])) < temp:
            temp = (abs(arr[i] - arr[i+1]))
    return temp


test = open("test2.txt", "r")
a = []
for i in test:
    a.append(i)
n = (a[0])

arr = list(map(int, a[1].rstrip().split()))

result = minimumAbsoluteDifference(arr)

print(result)
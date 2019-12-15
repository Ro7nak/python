import math
import os
import random_app_demo
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):

    '''
    if (arr.length == 0) return 0;
    arr[0] = Math.max(0, arr[0]);
    if (arr.length == 1) return arr[0];
    arr[1] = Math.max(arr[0], arr[1]);
    for (int i = 2; i < arr.length; i++)
      arr[i] = Math.max(arr[i-1], arr[i]+arr[i-2]);
    return arr[arr.length-1];
    '''
    print(arr)
    if len(arr) == 0:
        return 0
    arr[0] = max(0, arr[0])
    if len(arr) == 1:
        return arr[0]
    arr[1] = max(arr[0], arr[1])
    # print(arr[0])
    for i in range(2, len(arr)):
        arr[i] = max(arr[i - 1], arr[i] + arr[i - 2])
    print(arr)
    return arr[len(arr) - 1]

test = open("test2.txt", "r")
a = []
for i in test:
    a.append(i)
n = int(a[0])

arr = list(map(int, a[1].split()))

res = maxSubsetSum(arr)
print(res)

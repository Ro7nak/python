'''
You are given an array of  integers, , and a positive integer, . Find and print the number of  pairs where  and  +  is divisible by .

For example,  and . Our three pairs meeting the criteria are  and .

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

n: the integer length of array
ar: an array of integers
k: the integer to divide the pair sum by
'''

import math
import os
import random
import re
import sys



# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    a = ar.copy()
    print(a)
    count = 0
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            z = (a[i] + ar[j])
            # print(z)
            if (z % k) == 0:
                count += 1
    return count


nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(result)

'''
 ex of sample input
  ex of sample input
'''
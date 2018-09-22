import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    a = []
    b = []
    for i in s1:
        a.append(i)
    for j in s2:
        b.append(j)
    # print(a)
    # print(b)
    a.sort()
    b.sort()
    for x in a:
        for i in b:
            if i == x:
                return"YES"
    return "NO"


if __name__ == '__main__':
    test = open("test3.txt", "r")
    a = []
    for i in test:
        a.append(i)

    q = int(a[0])
    x = a[1::2]
    y = a[2::2]
    for q_itr in range(q):
        result = twoStrings(x[q_itr], y[q_itr])

        print(result + '\n')

# https://www.hackerrank.com/challenges/time-conversion/problem

import os
import sys


def timeConversion(s):
    if (s[8:]) == "AM":
        if s[:2] == "12":
            return "00" + s[2:8]
        else:
            return s[:8]
    else:
        if s[:2] == "12":
            return s[:8]
        else:
            return str(int(s[:2]) + 12) + s[2:8]


s = input()
result = timeConversion(s)
print(result)

'''
sample input:
07:05:45PM
12:40:22AM
06:40:03AM
12:45:54PM
'''
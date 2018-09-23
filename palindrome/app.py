import math
import os
import random
import re
import sys


def substrCount(n, s):
    l = []
    count = 0
    cur = None

    # 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0

    # 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

    # 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans


'''
def substrCount(n, s):
    char_freqs = [(s[0], 1)]
    for i in range(1, len(s)):
        char = s[i]
        if char == char_freqs[-1][0]:
            char_freqs[-1] = (char, char_freqs[-1][1] + 1)
        else:
            char_freqs.append((char, 1))
    print(char_freqs)

    total = 0
    for i in range(0, len(char_freqs)):
        val = char_freqs[i][1]
        # e.g. `(a, 4)`
        if val > 1:
            total += val * (val + 1) / 2
        # e.g. `[(a, 4), (b, 1), (a, 4)]`
        elif i > 0 and i < len(char_freqs) - 1 and val == 1:
            total += 1
            if char_freqs[i-1][0] == char_freqs[i+1][0]:
                total += 1
        else:
            total += 1

    print(total)
    return int(total)
'''

test = open("test.txt.txt", "r")

a = []
for i in test:
    a.append(i)

for i in range(int(a[0])):
    s = a[1].split()

    print(s)
    result = substrCount(int(s[0]), s[1])
    print(result)

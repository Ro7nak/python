import math
import os
import random_app_demo
import re
import sys
from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note.sort()
    magazine.sort()
    count = 0
    # print(Counter(magazine))
    # print(Counter(note))
    # print(Counter(note)-Counter(magazine))
    z = len(note)
    for i in note:
        if i in magazine:
            a = magazine.index(i)
            magazine.pop(a)
            count += 1
    if count == z:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    test = open("test_case.txt", "r")
    a = []
    for i in test:
        a.append(i)
    mn = a[0].split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = a[1].rstrip().split()

    note = a[2].rstrip().split()

    checkMagazine(magazine, note)

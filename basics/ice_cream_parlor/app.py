import math
import os
import random_app_demo
import re
import sys


# Complete the whatFlavors function below.
def whatFlavors(cost, money):

    for i in range(len(cost)):
        for j in range(1 + i, len(cost)):
            if cost[i] + cost[j] == money:
                print(str(i + 1) + " " + str(j + 1))
                break


test = open("test2.txt", "r")
a = []
for i in test:
    a.append(i)
t = int(a[0])
for i in range(t):
    money = int(a[1 + (i * 3)])
    n = int(a[2 + (i * 3)])
    cost = list(map(int, a[3 + (i * 3)].rstrip().split()))
    print(cost)
    whatFlavors(cost, money)

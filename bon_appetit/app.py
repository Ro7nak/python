import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    a = bill
    a.remove(a[k])
    #print(a)
    sum = 0
    for i in a:
        sum += i
    #print(sum/2)
    x = b-int(sum/2)
    if x == 0:
        print("Bon Appetit")
    else:
        print(x)

if __name__ == '__main__':
    test = open("test.txt", "r")
    a = []
    for i in test:
        a.append(i)
    nk = a[0].rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, a[1].rstrip().split()))

    b = int(a[2].strip())

    bonAppetit(bill, k, b)

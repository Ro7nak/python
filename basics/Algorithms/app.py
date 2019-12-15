'''
link - https://stackoverflow.com/questions/2840593/how-do-i-find-the-millionth-number-in-the-series-2-3-4-6-9-13-19-28-42-63

HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly  people on social media.

On the first day, half of those  people (i.e., ) like the advertisement and each shares it with  of their friends. At the beginning of the second day,  people receive the advertisement.

Each day,  of the recipients like the advertisement and will share it with friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day .

For example, assume you want to know how many have liked the ad by the end of the  day.

Day Shared Liked Cumulative
1      5     2       2
2      6     3       5
3      9     4       9
4     12     6      15
5     18     9      24
The cumulative number of likes is .
'''

import math
import os
import random_app_demo
import re
import sys


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    x = []
    x.append(2)
    for i in range(n - 1):
        x.append(math.floor(3 * x[i] / 2))
    return sum(x)

    '''
    m = [2]
    for i in range(int(n)-1):
        m.append(int(3*m[i]/2))
    return (sum(m))
    '''


n = int(input())

result = viralAdvertising(n)

print(result)

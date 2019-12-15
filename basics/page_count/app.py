'''
Brie’s Drawing teacher asks her class to open their books to a page number. Brie can either start turning pages from the front of the book or from the back of the book. She always turns pages one at a time. When she opens the book, page  is always on the right side:

image

When she flips page , she sees pages  and . Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is  pages long, and she wants to turn to page , what is the minimum number of pages she will turn? She can start at the beginning or the end of the book.

Given  and , find and print the minimum number of pages Brie must turn in order to arrive at page .
'''

import os
import sys


def pageCount(n, p):
    return (min(p//2, n//2 - p//2))
    '''
    def solve(n, p):
        pages_to_back = n-p
        turns_from_front = -(-(p-1) // 2)
        if n % 2 != 0:
            turns_from_back = -(-(pages_to_back - 1) // 2)
        else:
            turns_from_back = -(-(pages_to_back) // 2)
        turns = [turns_from_front, turns_from_back]
        return min(turns)
    '''

test = open("test.txt", "r")
a = []
for i in test:
    a.append(i)

n = int(a[0])

p = int(a[1])

result = pageCount(n, p)
print(result)

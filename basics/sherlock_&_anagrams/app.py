import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(string):
    hash_table = dict()
    hashes = dict()

    def prime_map(c):
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
        return primes[ord(c) - ord('a')]

    def get_hash(s):
        if s in hashes:
            hash_val = hashes[s]
        else:
            hash_val = 1

            for c in s:
                hash_val *= prime_map(c)

            hashes[s] = hash_val

        return hash_val

    def save_hash(hash_val1, s):
        hash_val = get_hash(s)
        if hash_val1 == hash_val:
            if hash_val in hash_table:
                hash_table[hash_val] += 1
            else:
                hash_table[hash_val] = 1

    lenS = len(string)
    for length in range(1, lenS):
        for i in range(0, lenS - length):
            substr1 = string[i:i + length]
            hash1 = get_hash(substr1)
            for j in range(i + 1, lenS - length + 1):
                substr2 = string[j:j + length]
                save_hash(hash1, substr2)

    return sum([v for (k, v) in hash_table.items()])


test = open("test2.txt", "r")
a = []
for i in test:
    a.append(i)
q = int(a[0])
for i in range(1, q+1):
    s = a[i].rstrip()
    result = sherlockAndAnagrams(s)
    print(str(result))

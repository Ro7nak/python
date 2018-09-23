from math import fabs
from collections import Counter
z = "abcdefth"
b = "defbc"
letterArray = [0] * 26
#print(letterArray)
a = ord('d')-ord('a')

sam = "abcdefghhgfedecba"
s= Counter(sam)
print(max(s.elements()))
s.keys()
print(17/(len(sam)*8))
print(17 % len(sam))

sa = "aabbcd"
print(6/(len(sa)*2))
print(6 % len(sa))

print(sorted(sam))
#print(int(fabs(a)))

one_series = []
for i in range(10):
   one_series.append((10**i)//9)
print(one_series)

from collections import Counter

def encode(s):
    a = list(map(str, s))
    k = Counter(s)
    print(a)
    for i in range(len(k)):
        d = k.popitem()
        print(str(d[1])+d[0], end="")


encode("rroijgghgg")




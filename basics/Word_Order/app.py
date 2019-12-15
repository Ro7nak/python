from collections import Counter
test = open("test.txt", "r")
z = []
for i in test:
    z.append(i)
# print(z)
n = int(z[0])
a = []
for i in range(1, n+1):
    a.append(z[i].rstrip())
a = Counter(a)
print(len(a))
for i in range(n-1):
    print(a.most_common()[i][1], end=" ")

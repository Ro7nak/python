from itertools import product
a = input().split()
b = input().split()
#a = map(int, input().split())
for x in range(len(a)):
    a[x] = int(a[x])
for y in range(len(b)):
    b[y] = int(b[y])
# c = [a, b]
print (*product(a, b))

# example 1 2
#         3 4
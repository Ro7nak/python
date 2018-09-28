a = [10, 20, 55, 63, 96]
a1 = []
print(a)
b = a.copy()
for i in range(len(a)):
        reverse = 0
        while a[i] >0:
            n = a[i] % 10
            reverse = (reverse*10) + n
            a[i] = a[i] // 10
        a1.append(reverse)

for i in range(len(b)):
    print(int(str(b[i])[::-1]))

print(a1)
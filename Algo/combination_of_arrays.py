def maxMin(k, arr):
    unfairness = 0
    arr.sort()
    b= []
    a = list(map(int, arr))
    for i in combinations(arr, k):
        b.append(i)

# refer max min python project for more info

'''
input-
4
1
2
3
4
10
20
30
40
100
200

output -
[(1, 2, 3), (1, 2, 4), (1, 2, 10), (1, 2, 20), (1, 2, 30), (1, 2, 40), (1, 2, 100), (1, 2, 200), (1, 3, 4), (1, 3, 10), (1, 3, 20), (1, 3, 30), (1, 3, 40), (1, 3, 100), (1, 3, 200), (1, 4, 10), (1, 4, 20), (1, 4, 30), (1, 4, 40), (1, 4, 100), (1, 4, 200), (1, 10, 20), (1, 10, 30), (1, 10, 40), (1, 10, 100), (1, 10, 200), (1, 20, 30), (1, 20, 40), (1, 20, 100), (1, 20, 200), (1, 30, 40), (1, 30, 100), (1, 30, 200), (1, 40, 100), (1, 40, 200), (1, 100, 200), (2, 3, 4), (2, 3, 10), (2, 3, 20), (2, 3, 30), (2, 3, 40), (2, 3, 100), (2, 3, 200), (2, 4, 10), (2, 4, 20), (2, 4, 30), (2, 4, 40), (2, 4, 100), (2, 4, 200), (2, 10, 20), (2, 10, 30), (2, 10, 40), (2, 10, 100), (2, 10, 200), (2, 20, 30), (2, 20, 40), (2, 20, 100), (2, 20, 200), (2, 30, 40), (2, 30, 100), (2, 30, 200), (2, 40, 100), (2, 40, 200), (2, 100, 200), (3, 4, 10), (3, 4, 20), (3, 4, 30), (3, 4, 40), (3, 4, 100), (3, 4, 200), (3, 10, 20), (3, 10, 30), (3, 10, 40), (3, 10, 100), (3, 10, 200), (3, 20, 30), (3, 20, 40), (3, 20, 100), (3, 20, 200), (3, 30, 40), (3, 30, 100), (3, 30, 200), (3, 40, 100), (3, 40, 200), (3, 100, 200), (4, 10, 20), (4, 10, 30), (4, 10, 40), (4, 10, 100), (4, 10, 200), (4, 20, 30), (4, 20, 40), (4, 20, 100), (4, 20, 200), (4, 30, 40), (4, 30, 100), (4, 30, 200), (4, 40, 100), (4, 40, 200), (4, 100, 200), (10, 20, 30), (10, 20, 40), (10, 20, 100), (10, 20, 200), (10, 30, 40), (10, 30, 100), (10, 30, 200), (10, 40, 100), (10, 40, 200), (10, 100, 200), (20, 30, 40), (20, 30, 100), (20, 30, 200), (20, 40, 100), (20, 40, 200), (20, 100, 200), (30, 40, 100), (30, 40, 200), (30, 100, 200), (40, 100, 200)]
'''
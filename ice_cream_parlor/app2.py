def whatFlavors(cost, money):
    map = []
    for pos in range(len(cost)):
        f1 = cost[pos]
        f2 = money - f1
        if f2 in map:
            # print(f2)
            print(cost.index(f2) + 1, pos + 1)
        else:
            map.append(f1)
        #print(map)

'''
def get_flavours(money,flavours):
    map = {}
    for pos, cost in enumerate(flavours):
        if cost in map:
            return (map[cost], pos + 1)
        else:
            map[money-cost] = pos + 1
'''

test = open("test2.txt", "r")
a = []
for i in test:
    a.append(i)
t = int(a[0])
for i in range(t):
    money = int(a[1 + (i * 3)])
    n = int(a[2 + (i * 3)])
    cost = list(map(int, a[3 + (i * 3)].rstrip().split()))
    print(cost)
    whatFlavors(cost, money)
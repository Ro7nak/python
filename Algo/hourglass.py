k = int(input("enter number: "))
for i in range(k):  # for upper
    for j in range(i):
        print(" ", end="")
    for z in range(k-i):
        print("* ", end="")
    print("\r")
for a in range(k-1):  # for lower
    for b in range(k-2-a):
        print(" ", end="")
    for c in range(a+2):
        print("* ", end="")
    print("\r")

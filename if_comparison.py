
def max_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(max_num(2, 6, 9))

def equal(a, b):
    if a == b:
        return print("both numbers are equal")
    else:
        return print("both numbers are not equal")

equal(5, 5)

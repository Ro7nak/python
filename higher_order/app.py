def add(x, y):
    return x + y
def call_function(func1, a, b):
    ret = func1(a, b)
    return ret
print(call_function(add, 10, 20))



def ret_function(a, b):
    a = a * a
    b = b * b
    return lambda: a + b
new_func = ret_function(2, 3);
print(new_func())

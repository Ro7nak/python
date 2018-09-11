print(2 ** 3)


def square(base_num, power_num):
    result = 1
    for int in range(power_num):
        result = result * base_num
    return result


print(square(2, 3))

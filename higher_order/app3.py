def add(data):
    return data+2
def prod(data):
    return data*2
def main_fun(function1,function2, number_list):
    result_sum=0
    for num in number_list:
        if(num%3==0):
            result_sum=result_sum+function1(num)
        else:
            result_sum=result_sum+function2(num)
    return result_sum
number_list=[1,3,5,6]
print(main_fun(add, prod, number_list))
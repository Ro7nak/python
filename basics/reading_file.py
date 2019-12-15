
employee_file = open("e1.txt", "r")
# r for read, w for write, a for append, r+ read and write

print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())

# print(employee_file.readlines())  # will give eac line in a array

for emp in employee_file.readlines():
    print(emp)

employee_file.close()
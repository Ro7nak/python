
employee_file = open("e1.txt", "a")  # w will overwrite old file

# print(employee_file.read())

# employee_file.write("\nToby - Human resources")
#employee_file.write("\nKelly - Customer Service")


employee_file.close()


emp_file = open("employee.txt", "w")

emp_file.write("\nKelly - Customer Service")
emp_file.close()

html = open("index.html", "w")

html.write("<p> This is HTML</p>")

html.close()
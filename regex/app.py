import re

print(re.search("an", "rounak goyanka"))

if(re.search(r"Air","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"A..l","Aopline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"A\dl","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"A[4-8]l","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"Hell|Fell","Fellow")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"Air\s","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"A\d*","A2234line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"A\d+","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"A\d?i","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"A\d{3}i","A223irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"^A","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"e$","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"\w$","Airline%")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"\*","Air*line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# Replaces Flight with Plane
flight_details="Flight Savana Airlines a2134"
print(re.sub(r"Flight",r"Plane",flight_details))

# () is used to group characters. Here we are grouping 4 numbers together and referring it as \1. 1 indicates the first group
flight_details="Flight Savana Airlines a2134"
print(re.sub(r"a(\d{4})",r"A\1",flight_details))
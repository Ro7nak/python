
for letter in "Draft":
    print(letter)

classes = ["science", "maths", "English"]
for clas in classes:
    print(clas)

for index in range(10):
    print(index)

for index in range(3, 10):  # 3 will be included but 10 will not be included
    print(index)

for index in range(len(classes)):
    print(classes[index])


for index in range(5):
    if index == 0:
        print("like")
    else:
        print("don't like")

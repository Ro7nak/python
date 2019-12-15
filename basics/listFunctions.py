
lucky_number = [7, 5, 3, 15, 77, 1]
friends = ["Joao", "Jack", "Claudia", "Gerardo", "Leo", "Lukasz"]

# print(lucky_number.sort(lucky_number))

# friends.extend(lucky_number)  # merge two list
# print(friends)
friends.append("Murat")

print(friends)

friends.append("Rounak")  # add element at end of list
print(friends)

friends.insert(1, "Jaroslaw")  # insert element in specified index in list
print(friends)

friends.remove("Joao")  # remove element from list

print(friends)

print(friends.index("Rounak"))  # will give index of value passes

friends.pop()  # remove last element
print(friends)

friends.sort()
print(friends)

friends.reverse()  # sort in reverse order
print(friends)

work = friends.copy()
print(work)

friends.clear()
print(friends)

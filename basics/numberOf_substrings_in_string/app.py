def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i:(len(sub_string) + i)] == sub_string:
            count += 1
    return count

# (sum([1 for i in range(0, len(string) - len(sub_string) + 1) if (string[i:(len(sub_string)+i)] == sub_string)]))

if __name__ == '__main__':
    test = open("test.txt", "r")
    a=[]
    for i in test:
        a.append(i)
    string = a[0].strip()
    sub_string = a[1].strip()

    count = count_substring(string, sub_string)
    print(count)
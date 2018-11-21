def time_conversion(s):
    if int(s[:2]) > 12:
        if int(s[:2]) == 24:
            return "00" + s[2:] + "AM"
        else:
            return str(int(s[:2]) - 12) + s[2:] + " PM"
    else:
        return s + " AM"


s = input()
result = time_conversion(s)
print(result)

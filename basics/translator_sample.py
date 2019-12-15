def translate(phrase):
    result = ""
    for char in phrase:
        if char in "aeiouAEIOU":
            if char.isupper():
                result = result + "G"
            else:
                result = result + "g"
        else:
            result = result + char
    return result


print(translate(input("Enter a phrase to translate: ")))

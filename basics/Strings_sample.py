print("rom = read only memory")
print("rom \" read only memory")
print("rom \n read only memory")
print("rom = read only memory")

phrase = "ROM"
        # 012
print(phrase + "= read only memory")

print(phrase.lower())
print(phrase.upper())

print(phrase.isupper())
print(phrase.lower().isupper())
print(len(phrase))
print(phrase[0])  # char at 0 index
print(phrase.lower().index("r"))

print(phrase.replace("O", "A"))


name = "Raghav"

print(name.count("a"))
print(name.replace("a", "A"))
print(name.find("a"))
print(name.startswith("Ra"))
print(name.endswith("ha"))
print(name.isdigit())
print(name.split("a"))

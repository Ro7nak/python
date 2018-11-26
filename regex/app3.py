import re
word="Indian Airlines4"
if re.search(r"^I", word) and re.search(r"e$", word):
    print(re.sub(r"Indian",r"Singapore",word))
else:
    print(re.sub(r"s(\d{1})",r"S\1",word))

# encrypt
user_input = input("Enter string: ")
cipher_text = ''  # add all values to string
for char in user_input:  # for every character in input
    cipher_num = (ord(char)) + 3 % 26  # using ordinal to find the number
    # cipher = ''
    cipher = chr(cipher_num)  # using chr to convert back to a letter
    cipher_text = (cipher_text + cipher)
print(cipher_text)

# decrypt
decrypt_text = ''
for char in cipher_text:  # for every character in the encrpted text
    decrypt_num = (ord(char)) - 3 % 26
    # decrypt = ''
    decrypt = chr(decrypt_num)
    decrypt_text = (decrypt_text + decrypt)
print(decrypt_text)

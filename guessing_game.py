secret_word = "draft"
guess = ""

# while guess != secret_word:
#    guess = input("enter secret word: ")

# print("correct")

count = 0
limit = 5
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if count < limit:
        guess = input("enter secret word: ")
        count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses, you lose!")
else:
    print("correct, you win!")

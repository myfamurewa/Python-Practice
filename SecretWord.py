secret_word = "Avacado"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a guess:")
        guess_count += 1
        if guess_count == 1:
             print("Here's a hint it has a pit")
        elif guess_count == 2:
            print("Heres' hint number 2: It's used to make guacamole")
        elif guess_count == 3:
            print("Come on! You should have gotten it by now")
    else:
        out_of_guesses = True
if out_of_guesses == True:
    print("You lose!")
else:
    print("You win!")
replay = input("Do you want to play again:")
if replay == "yes" or "Yes":
    print("I'm not sure how to get it to replay yet")
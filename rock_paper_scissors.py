import random

# fie i/o function  for historical results
def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results(w, d, l):
    text_file = open("history.txt", "w")
    text_file.write( str(w) + "," + str(d) + "," + str(l))
    text_file.close()


#welcome message
results = load_results()
wins = int(results[0])
draws = int(results[1])
losses = int(results[2])
print("welcome to Rock, Paper, Scissors!")
print("Wins: %s, Draws: %s, Losses: %s" % (wins, draws, losses))
print("please choose to continue...")

#initialize user, computer choices
computer = random.randint(1,3)
user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))

#gameplay loop
while not user == 9:
    #Rock
    if user == 1:
        if computer == 1:
            print("computer chose rock ... tie!")
            draws += 1
        elif computer == 2:
            print("computer chose paper ... computer wins")
            losses += 1
        elif computer == 3:
            print("computer chose scissors ... you win!!!!")
            wins += 1
    elif user == 2:
        if computer == 2:
            print("computer chose paper... tie!")
            draws += 1
        elif computer == 3:
            print("computer chose scissors ... computer wins")
            losses += 1
        elif computer == 1:
            print("computer chose rock ... you win!!!!")
            wins += 1
    elif user == 3:
        if computer == 3:
            print("computer chose scissors ... tie!")
            draws += 1
        elif computer == 1:
            print("computer chose rock ... computer wins")
            losses += 1
        elif computer == 2:
            print("computer chose paper ... you win!!!!")
            wins += 1
    else:
        print("invalid input please select one of the four options")
        user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))
    #print updated stats
    print("Wins: %s, Draws: %s, Losses: %s" % (wins, draws, losses))

    #promp user to make another selection
    print("please choose to continue...")
    #initialize user, computer choices again
    computer = random.randint(1,3)
    user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))
save_results(wins, draws, losses)
    
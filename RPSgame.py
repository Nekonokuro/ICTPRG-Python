import random

score_human = 0
score_machine = 0

choices = ["rock", "paper", "scissors"]
print("Rock wins sciccors. Scissors cut paper. Paper covers rock.")

player = input("Choose rock, paper or scissors. If you want to quit, print 'Quit': \n")


while player == True:
    player = player.lower()
    computer = random.choice(choices)
    print("You chose " + player + "\nOpponent chose " + computer + ".")
    if player == computer:
        print("Tie!")
    elif player =="rock":
        if computer == "scissors":
            print("You win!")
            score_human = score_machine + 1
        else:
            print("Opponent wins!")
            score_machine = score_machine + 1
        print ("Your score is: ", str(score_human), "\nOpponent score is: ", str(score_machine))
    elif player == "paper":
        if computer == "rock":
            print ("You win!")
            score_human = score_human + 1
        else:
            print("Opponent wins!")
            score_machine = score_machine + 1
        print ("Your score is: ", str(score_human), "\nOpponent score is: ", str(score_machine))
    elif player == "paper":
        if computer == "rock":
            print ("You win!")
            score_human = score_human + 1
        else:
            print ("Opponent wins!")
            score_machine = score_machine + 1
        print ("Your score is: ", str(score_human), "\nOpponent score is: ", str(score_machine))
    elif player == "scissors":
        if computer == "paper":
            print ("You win!")
            score_human = score_human + 1
        else:
            print ("Opponent wins!")
            score_machine = score_machine + 1
        print ("Your score is: ", str(score_human), "\nOpponent score is: ", str(score_machine))
    else:
        print ("Error")
        player = input ("Choose rock, paper or scissors. If you want to quit, print 'Quit': \n")
import random

ran_num = random.randint(1, 25)  
guesses = 0
guess_log = []  
print("Hey there! Lets play a little guessing game." + "\nGuess the number between 1 and 25")
while guesses < 7: 
    user_guess = int(input("Enter guess:\n"))
    guesses += 1
    count_guess = 7 - int(guesses)
    guess_log.append(user_guess)
    if user_guess == ran_num:  
        print("Damn, You win!" + "\nThe number was indeed " + str(ran_num) + "\nYou guessed in " + str(guesses) + " guesses")
        break 
    elif user_guess < ran_num: 
        print("Nope, it is greater than " + str(user_guess) + "\nYou have " + str(count_guess) + " guesses left!")         
    else: 
        print("Nope, it is less than " +  str(user_guess) + "\nYou have " + str(count_guess) + " left!")           
if not guesses < 7: 
    print("AHAHA! YOU LOOSE!" + "\nThe number was " +  str(ran_num))

print("Your guess log: " + "\n" + str(guess_log)) 

#Design a program that simulates the toss of a coin. It generates 1 and 2 .
#Designate 1 as head and 2 as tail. Import random function and use randint option. 
#Toss the coin 10 times. Count the number of heads and tails and print them. 	
#Modify the program and use a while loop with an option to let the user quit the loop when needed.   
#Count the number of tosses and the number of times heads and tails appear. 

import random

toss_count = 0
tails_count = 0
heads_count = 0
while True:
    user_toss = str(input("Enter any key or 'q' to quit game"))
    if user_toss != "q":
        for x in range (1,11):
            toss = random.randint(1, 2)
            if toss == 1:
                heads_count = heads_count + 1
                print("Heads counted: " + str(heads_count))
            else:
                tails_count = tails_count + 1
                print("Tails counted: " + str(tails_count)) 
                toss_count = toss_count + 1

    else:
        toss_count = toss_count + 1
        print("Tails total number: " + str(tails_count)) 
        print("Heads total number: " + str(heads_count))               
        break


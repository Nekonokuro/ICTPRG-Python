#On a roulette wheel, the pockets are numbered from 0 to 36. The colours of the pockets are as follows:
#Pocket 0 is green.
#For pockets 1 through 10, the odd numbered pockets are blue and the even numbered pockets are black
#For pockets 11 through 18, the odd numbered pockets are black and the even numbered pockets are blue
#For pockets 19 through 28, the odd numbered pockets are blue  and the even numbered pockets are black
#For pockets 29 through 36, the odd numbered pockets are black and the even numbered pockets are blue.
#Write a program that asks the user to enter a pocket number and displays where a pocket is green, blue or black

#Modify this program such that the program loops through using a while statement until the user enters a negative number. 
# It also prints how many numbers were entered.


#pock_num = int(input("Enter a pocket number 0 to 36: "))
count_num = 0
while True:
    pock_num = int(input("Enter a pocket number 0 to 36: "))
    if pock_num>36:
        print("Error!")
    elif pock_num==0:
        colour = "Green"
    elif pock_num>=1 and pock_num<=10:
        if pock_num %2 == 0:
            colour = "Black"
        else:
            colour = "Blue"
    elif pock_num>=11 and pock_num<=18:
        if pock_num %2 == 0:
            colour = "Blue"
        else:
            colour = "Black"
    elif pock_num>=19 and pock_num<=28:
        if pock_num %2 == 0:
                colour = "Black"
        else:
            colour = "Blue"
    if pock_num<0:
        print("Critical error. Quitting program")
        break
    else:
        count_num = count_num + 1
        print("Number " + str(pock_num) + " is " + str(colour)) 
            
print("Total numbers entred: " + str(count_num))
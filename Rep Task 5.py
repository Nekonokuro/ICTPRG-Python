#Write a code that prompts the user to enter a number in the range of 1 through 100 and validates the input.

#num = int(input("Enter a number from 1 to 100 "))

    #if num>1 and num<100:
        #print("You entered " + str(num))
    #else:
        #print("Error.You should enter a number between 1 and 100 ")


#while num<1 and num>100:
    #print("Error.You should enter a number between 1 and 100")
    #score=int (input ("Enter a number from 1 to 100 "))

while True:
    
    num = int(input("Enter number 1 to 100: "))
    if num>1 and num<100:
        print("You entered " + str(num))
    else:
        print("Error. Wrong number.")


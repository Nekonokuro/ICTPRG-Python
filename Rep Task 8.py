#In Mathematics the notation n! represents the factorial of a non-negative integer n. 
#The factorial of n is the product of all non-negative integers from 1 to n
#Eg      4! = 1x2x3x4= 24
#Write a program that lets the user enter a nonnegative integer and then uses the loop to calculate the factorial of that number. 
# Print the factorial.

while True:
    num = int(input("Enter a number: "))
    fact = 1
    if num<0:
        print("Error. You entered negative number")
    elif num==0:
        print("The factorial is 1")
    else:
        for i in range(1,num + 1):
            fact = fact*i
        print("The factorial of ", num, "is", fact)



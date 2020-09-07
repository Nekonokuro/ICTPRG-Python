#Write a program that asks the user for three scores out of 100. It then calculates the average. If the average is greater than 90, congratulate the user. 
#Write a pseudocode before you write the Python program.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: ")) 
sum_numbers = num1 + num2 + num3
average = sum_numbers / 3

if average>90:
    print("Congratulations!")
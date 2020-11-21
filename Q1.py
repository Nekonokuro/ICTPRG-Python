#Write a python script that ask for two numbers, add them together and output the response into a file called 'maths.txt'. 


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
total = num1 + num2

with open("maths.txt", "w") as math_file:
    math_file.write(str(total))
    


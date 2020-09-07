#1. Write a loop that lets the user enter a number. The number should be multiplied by 10 and result will be assigned to a variable name prod. 
#The loop should iterate as long as the product is less than 100

product = 0

while product < 100:
    num = int(input("Enter a number: "))
    product = num * 10

#Write a loop that calculates the total of the following series of numbers.
#1/15 + 2/14 + 3/13 + 4/12 + - - -  15/1
#Hint: define two variables x and y and calculate the ratio x/y.

#x = int(input("Enter 1st number: "))
#y = int(input("Enter 2nd number: "))
#ratio = x / y

#while True:
    #num_ser_x = x + 1
    #num_ser_y = y - 1
    #num_ser = num_ser_x / num_ser_y
    #print("Total: " + str(num_ser))    

total = 0
for x in range(1,15):
    total += x / (15 - x)
print("Total: " + str(total))
#Write program with a while loop that ask the user to enter a series of positive numbers . 
#The user should enter a negative number to signal the end of the series. 
#The program should display the sum of the numbers after it quits the loop.

sum_num=0

while True:
    num = int(input("Enter a positive number. To quit and calculate sum, enter negative number. "))
    if num>=0:
        sum_num=sum_num + int(num)     
    else:
        break
print("Total:" + str(sum_num))
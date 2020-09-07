#Write a program that can accept many numbers from the user, until they enter an x. Example:

#Enter a number: 5
#Enter a number: 9
#Enter a number: 3
#Enter a number: 12
#Enter a number: x
#You entered: [5, 9, 3, 12]


num_list = []
while True:
    num = input("Enter a number: ")
    if num !="x":
        num_list.append(int(num))
    else:
        break
print("You entered: " + str(num_list))
        
 


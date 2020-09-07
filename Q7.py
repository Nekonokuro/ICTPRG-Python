#Write a program to ask the user for numbers, and then print any repeating numbers in a list. Example:

#Enter a number: 5
#Enter a number: 2
#Enter a number: 6
#Enter a number: 98
#Enter a number: 7
#Enter a number: 6
#Enter a number: 5
#Enter a number: x
#Repeating numbers: [5, 6]

import collections 

list_num = []
num = input("Press key to start")
print("Starting")
while num !="x":
    num = input("Enter number: ")
    list_num.append(num)

print([item for item, count in collections.Counter(list_num).items() if count > 1])



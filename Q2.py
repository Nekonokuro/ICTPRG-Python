#Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019
#The date will be printed like below:
#Date: 23
#Month : 08
#Year: 2019

date = input("Enter the date in format dd/mm/yyyy: \n")
date_list = date.split("/")
print("Date: " + date_list[0] + "\n" + "Month: " + date_list[1] + "\n" + "Year: " + date_list[2])


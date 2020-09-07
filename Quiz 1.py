#Write a program that asks the user for their name, 
# checks if their name is either "frank" or "george" and if it is, greet them by their name.

username = str(input("Enter your username: "))
list_approved_names = ["Frank", "George"]

if username in list_approved_names:
    print("Welcome, " + username + "!")
else:
    print("Access denied!")    
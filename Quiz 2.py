#Write a program that asks the user for their year of birth, checks if they are of legal drinking age, 
# and tells the user to come into the bar. Example:
#What is your Year of birth: 1995
#You are: 25 Years old
#Come in and have a drink!

#What is your Year of birth: 2003
#You are: 17 Years old
#Go away. Child.


user_birth = input("What is your year of birth: ")
user_age = int(2020 - int(user_birth))
print("You are " + str(user_age) + " years old")

if user_age>=18:
    print("Come in and and have a drink!")
else:
    how_long_wait = int(user_birth) - 2002
    print("Not today, come back in " + str(how_long_wait) + " years!")    


#Write a program to compare two strings. Get a password from the user. If the password is “Rela238#” accept the password.
 #Otherwise inform the user that the password is incorrect. Set the password using  a variable at the start of the program.




password = str("Rela238#")
user_pass = str(input("Please, enter your password: "))

if user_pass == password:
    print("Passwod accepted!")
else:
    print("Access denied!")


#Write a program that could be used for an (unsecure) login, with a username and password. For example:

#-------------------------------------
#Enter username: bob
#Enter password: password1234
#Access Granted!
#-------------------------------------
#Enter username: frank
#Enter password: invalidpass
#Access Denied!

username_list = ["Bob", "Mary", "Ivan"]
password_list = ["QWERTY", "qwerty", "thebestpassword"]
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

if username in username_list:
    if username == "Bob":
        if password == "QWERTY":
            print("Access granted!")
        else:
            print("Access denied!")
    elif username == "Mary":
        if password == "qwerty":
            print("Access granted!")
        else:
            print("Access denied!")
    elif username == "Ivan":
        if password == "thebestpassword":
            print("Access granted!")
        else:
            print("Access denied!")
else:
    print("Access denied!")                                     
   


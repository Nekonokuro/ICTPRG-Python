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
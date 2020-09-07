username_list = ["Bob", "Fred", "Lock"]
password_list = ["password1234", "happyPass122", "passwithlock44"]
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

if username in username_list:
    if username == [0]:
        if password == [0]:
            print("Access granted!")
        else:
            print("Access denied!")
    elif username == "Fred":
        if password == "happyPass122":
            print("Access granted!")
        else:
            print("Access denied!")
    elif username == "Lock":
        if password == "passwithlock44":
            print("Access granted!")
        else:
            print("Access denied!")
else:
    print("Access denied!")
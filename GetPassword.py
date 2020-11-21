import re

def GetPassword(password):

    pass_check = False

    while pass_check:

        password = input(password)
        
        if len(password) <7:
            print("Password length should be at at least 7 characters")
            continue
        elif not re.search("[a-z]", password):
            print("Password must contain lowercase letter")
            continue
        elif not re.search("[A-Z]", password):
            print("Password must contain uppercase letter")
            continue
        elif not re.search("[0-9]", password):
            print("Password must contain a number")
            continue
        elif not re.search("[!@#$%^&*()-_=+?/~]", password):
            print("Password must contain a special symbol: !@#$%^&*()-_=+?/~ ")
            continue
        elif "password" in password:
            print("Password should not contain word 'password' ")
            continue
        else:
            print("Password is valid")
            pass_check = True

    
user_pass = GetPassword("Enter you password.It must contain:\na lowercase letter\nan uppercase letter\na number\na symbol\nbe at least 7 charcter long\ndoes not contain word 'password'\n>>")


import re
pass_check = False

def GetEmailAddress(email):
    
    return re.match(r"[\w-]{2,32}@\w{2,32}\.\w{2,3}$", email)

while not pass_check:
    email = input("Enter your email: \n>>")
    valid_email = GetEmailAddress(email)
    if valid_email:
        print(f"Your email {email} is valid.")
        pass_check = True
    else:
        print(f"Your email {email} is invalid. Please, try again.")
        continue




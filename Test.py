#access = False
with open("logins.txt", "r") as check_file:
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    
    for check in check_file:
        u_name, u_pass = check.strip().split(":")
    if username == u_name and password == u_pass:
            print("Access granted!")
            
    else:
        print("Access denied!")
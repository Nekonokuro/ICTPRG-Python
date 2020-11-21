#Write a python script that asks for a username and password, then opens 'logins.txt' and 
#tries to find a valid ':' separated login from this file. eg:

#file:
#user4:password3

#python output:
#username? : user4 password?: password 3 Access Granted! 
username = 0
#with open("logins.txt", "w") as log_file:
    #while username != "":
        #username = str(input("Enter your username: ")).strip()
        #password = str(input("Enter your password: ")).strip()

        #log_file.write(username)
        #log_file.write(":")
        #log_file.write(password + "\n")
access = False
with open("logins.txt", "r") as check_file:
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    
    for check in check_file:
        u_name, u_pass = check.strip().split(":")
        if username == u_name and password == u_pass:
            print("Access granted!")
            access = True
            break
if not access:
    print("Access denied!")

#Write a python script that keeps asking for names, until they enter an empty name,
#then creates a file called 'people.txt' and adds names on a separate line. 

name = 0
with open("people.txt", "w") as filename:
    while name != "":
        name = input("Enter any name: \n")
        filename.writelines(str(name) + "\n")
        
    
#Write a program that enters a string containing a person's full name and then output their initials. Example:
#Full Name: Lachlan van der Velden
#Initials: LVDV
#Full Name: Dave Verg Douglas
#Initials: DVD

name = input("Enter your name: ")
name_list = name.split()

print("Full name: " + name + "\n" + "Initials: " + "".join(initial[0] for initial in name_list))




#Write a python script that reads a file called 'names.txt' 
#(which has names separated by a new line), then converts each name to the correct casing 
#and outputs them to a file called 'names-formated.txt' Eg:

with open("names.txt", "r") as names_file:

    for name in names_file:
        f_names = name.title()
        with open("names_formatted.txt", "a") as f_file:
            form_file = f_file.write(f_names)

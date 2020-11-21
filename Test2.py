file = open('names.txt', 'r')
for name in file:
    names = name.title()
    file = open('names-formated.txt', 'a')
file.write(names + "\n")
file.close()

ith open("names.txt", "r") as names_file:

    for name in names_file:
        f_names = name.title()
        with open("names_formatted.txt", "a") as f_file:
            form_file = f_file.write(f_names)

names = open('names.txt', 'r')
formatted = open('names-formatted.txt', '')

for line in names:
    fixed = line.title()
    formatted.write(fixed)

names.close()
formatted.close()

file1 = open("factorial.txt", "w")

for number in range (1,11):
    output = str(number) + ' = 1'
    factorial = 1

    for i in range (1,number + 1):
        factorial = factorial * i 
        if i > 1:
            output = str(output) + 'X' + str(i)
    output = str(output) + '->' + str(factorial)
    file1.write(str(output))
    file1.write('\n')
file1.close()
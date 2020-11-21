#Write a python script that outputs the factorial of all numbers from 1 - 10. eg:
#1 -> 1
#2 = 1x2 -> 2
#3 = 1x2x3 -> 6
#4 = 1x2x3x4 -> 24
with open("factorial.txt", "w") as fact_file:
    for number in range(1, 11):
        output = str(number) + "  "
        factorial = 1
        for i in range(1, number + 1):
    
            factorial = factorial * i
            output = str(number) + " = 1" + "X" + str(i)
            output = output + " -> " + str(factorial)
        print(output)
        fact_file.write(str(output) + "\n")
        


    
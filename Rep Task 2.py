#Design a repetition loop that ask for the number of times a loop should run. 
#In the loop, a number will be entered and a running total of the numbers entered in each iteration of the loop will be calculated. 
#This total will be printed once you exit the loop.

#total = 0
number = int(input("Enter a number: "))
num_loops = int(input("Enter the number of loops: "))

for x in range(num_loops):
    total = number * num_loops
print("Total: " + str(total))    

    

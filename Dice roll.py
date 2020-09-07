#Simulate the rolling of a die with 6 sides. You have to import the random module
#•	import random
#•	Generate a number 1 to 6. Set max_number to 6 and min_number to 1.
#•	You can decide how many times you want to roll the dice 
#•	Decide which of the numbers you want to add to a list countarray.  
#•	Add all the numbers rolled and store it in variable sum.
#•	When the required number of rolling of dice are done, you have to print the list with the selected numbers.
#•	Print the total of all numbers generated.

import random
max_number = 6
min_number = 1
count_list = []
total = 0
roll_times = int(input("How many time would you like to roll the dice?\n"))
print("Rolling the dice ...")
for roll in range(0, roll_times):
    roll_result = random.randint(int(min_number), int(max_number))
    total+=roll_result
    if roll_result>3:
        count_list.append(roll_result)   
print("Big scores: " + str(count_list))
print("Total score: " + str(total))

#THIS IS TEST CHANGE

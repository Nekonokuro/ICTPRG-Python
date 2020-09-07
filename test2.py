import random
max_number = 6
min_number = 1
count_list = []
total = 0
roll_times = int(input("How many time would you like to roll the dice?\n"))
print("Rolling the dice")
for roll in range(0, roll_times):
    roll_result = random.randint(int(min_number), int(max_number))
    total+=roll_result
    if roll_result>3:
        count_list.append(roll_result)   
print("Big scores: " + str(count_list))
print("Total score: " + str(total))
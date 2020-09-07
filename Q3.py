#Given the following python code
#values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
#Sum all of the numbers and output the result
#Average all of the numbers and output the result
#Output the maximum number in the list

values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]

values_sum = sum(values)
average = values_sum/len(values)
max_num = max(values)

print("Sum of numbers: " + str(values_sum) + "\n" + "Average of numbers: " + str(average) + "\n" + "Maximum number in a list: " + str(max_num))
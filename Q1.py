
#Given the following python code:
#values = [66, 43, 1, 6, 2, 99, 4]
#Output each number on a separate line if it is less than the number 10.

values = [66, 43, 1, 6, 2, 99, 4]
num_list =[numbers for numbers in values if numbers < 10]
print(*num_list, sep="\n")

#alter:

values = [66, 43, 1, 6, 2, 99, 4]
new_list = []
for item in values:
    if item < 10:
         new_list.append(item)
print(*new_list, sep = "\n")
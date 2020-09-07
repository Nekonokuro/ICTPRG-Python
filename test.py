digit = input('enter large number: ')
list_num = digit.split()
sum_num = sum(int(num) for num in str(digit))

print("Sum: " + "+".join(str(digit)) + '=' + str(sum_num))
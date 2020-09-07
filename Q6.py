
#Write a program that asks the user for a large number, and then sums all of the digits in that number: Example:
#Enter a large number: 29834892
#Sum of the digits: 2 + 9 + 8 + 3 + 4 + 8 + 9 + 2 = 45

large_number = input("Enter a large number: ")
sum_digits = sum(int(digit) for digit in str(large_number))
print("Sum of the digits: " + "+".join(str(large_number)) + "=" + str(sum_digits))

#digit = input('enter large number: ')
#list_num = digit.split()
#sum_num = sum(int(num) for num in str(digit))

#print("Sum: " + "+".join(str(digit)) + '=' + str(sum_num))
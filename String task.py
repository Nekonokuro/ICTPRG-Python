#Write a program that counts the number character in the sentence ‘The count of the character ‘c’ or ‘C’ in this sentence is needed’.
#Modify this program to count the number of Cs or c’s
#Hint: make the variable c_count

user_input = input("Enter a sentence: The count of the character ‘c’ or ‘C’ in this sentence is needed  \n")
char_num = len(user_input)
c_count = 0
for letter in user_input:
    if letter == "c" or letter == "C":
        c_count = c_count + 1

print("The number of character in the sentence is: " + str(char_num) + "\n" + "The number of C's and c's in the sentence is: " + str(c_count))


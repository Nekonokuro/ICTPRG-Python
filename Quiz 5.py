#Write a program that can grade a student based upon a percentage grade. Example:

#What was your grade: 99
#You will receive a "High Distinction"

#Please use the following grade table within your application:
#High Distinction 	100 - 90
#Distinction 	89- 80
#Credit 	79 - 70
#Pass 	69 - 50

A_score = 90
B_score = 80
C_score = 70
D_score = 50

grade = int(input("What was your grade: "))


if grade >= A_score:
    print("Congratulations! You got High Distinction!")
else:
    if grade >= B_score:
        print("Good grade, well done!")
    else:
        if grade >= C_score:
            print("Decent grade, not bad!")
        else:
            if grade >= D_score:
                print("Your grade is enough to pass!")
            else:
                print("You failed. Sorry")
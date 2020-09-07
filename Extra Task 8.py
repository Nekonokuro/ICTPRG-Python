#Modify this program with the value for the different scores

#A_score = 90
#B_score = 80
#C_score = 70
#D_score = 60
#Anything below 60 is F (fail)


A_score = 90
B_score = 80
C_score = 70
D_score = 60

score = int(input("Please, enter your score: "))


if score >= A_score:
    print("Your grade is A")
else:
    if score >= B_score:
        print("Your grade is B")
    else:
        if score >= C_score:
            print("Your grade is C")
        else:
            if score >= D_score:
                print("Your grade is D")
            else:
                print("Your grade is F")
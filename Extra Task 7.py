#Here is a code with many nested –if staements. The indendation is not correct. Rewrite the code such that the program works.


A_score = 80
B_score = 70
C_score = 50
D_score = 40

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






while True:
    try:
        score = int(input("Please enter your assignment score: "))
    except ValueError:
        print("Please enter right value - it should be a number only")
        continue
    else:
        break
if score >= 50: 
    print("You passed!Congratualtions!")
else:
    print("Sorry, you didn't pass. Try it again. Good luck!")


   


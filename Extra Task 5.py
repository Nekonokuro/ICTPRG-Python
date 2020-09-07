#Write a program that asks the user for the salary and the time in the job. 
#The minimum salary for the sanction of a bank loan is an annual salary of $50000 
#and the person has to be on the current job for at least 3 years. 
#The program should decide whether the person can be given a loan. Use nested if statement with else. 

salary = int(input("Please enter you salary, number only (e.g. 75500): "))
job_exp = int(input("Please, enter you jon experiens in full years: "))

if(salary >=50000):
    if(job_exp>=3):
        print("Loan approved!")
    else:
        print("Loan denied! More job experience is needed.")
else:
    if(job_exp>=3):
        print("Loan denied! Higher salary is needed")   
    else:
        print("Loan denied! Failed on salary and experience criteria")                    
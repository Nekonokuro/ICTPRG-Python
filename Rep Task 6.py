#A pathology staff collects samples each day for 5 days.
#Write a program that keeps a running total of the number of samples collected during 5 days. 
#The loop will ask for the number of samples collected for each day and when the loop is completed, 
#the program will display the total number of samples collected . 


num_days = 5
total = 0

for count in range(num_days):
    num_samples = int(input ("Enter the number of samples: "))
    total += num_samples

print("The total number of the samples collected: " + str(total))
    

#Write a set of nested loops that display 10 rows of   ‘*’ characters. 
#There should be 15 ‘*’ characters in each row

rows = 10
columns = 15
for r in range (rows):
    for c in range(columns):
        print('*', end='')
    print('')
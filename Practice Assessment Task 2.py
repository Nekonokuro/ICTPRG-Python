
with open("people.txt", "r") as ppl_file:
    for line in ppl_file:

        name, famname, age = line.strip().split("|")
        b_year = 2020 - int(age)
        low = name[0].lower()
        low_f = famname.lower()
        cap_f = famname.capitalize()
        up = name[0].upper()
        
        #if low != "b" and b_year < 1970:
        if  low != "b" and int(b_year) > 1970:
            userpass = low + low_f +"@DodnGy.net" + "|" + "!" + str(b_year) + cap_f + up + "_" + "\n"

            with open("userpass.txt", "a") as userpass_file:
                userpass_file.write(userpass)
        

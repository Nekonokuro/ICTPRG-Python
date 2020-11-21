def user_number(message):
    v_num = False
    while not v_num:
        try:
            num_input = int(input(message))
            print(f"You entered {num_input}. This is valid value") 
            v_num = True
            return num_input 
        except ValueError:
            print("You should enter valid value")
            continue
        
num = user_number("Enter a number: ")
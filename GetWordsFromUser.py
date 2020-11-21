
def get_words(message):
    min_words = 5
    max_words = 15
    words_count = False

    while not words_count:
        user_words = str(input(message)).strip().split(" ")
        
        if len(user_words) > max_words or len(user_words) < min_words:
            print(f"Your number of words should be within range {min_words} and {max_words}")
            continue
            return user_words 
              
        else:
            word_list = [w.lower() for w in user_words]
            print(f"Your words list is: {word_list}") 
            words_count = True
        
words = get_words("Enter words: ")

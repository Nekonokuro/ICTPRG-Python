pancakes = ["flour", "sugar", "eggs", "milk", "poison"]
for ingredient in pancakes:
    if ingredient == "poison":
        print("No, " + ingredient + " is a bad idea!")
        continue
    print(ingredient + " is right ingredient for pancakes")
print("We are ready to make pancakes!")




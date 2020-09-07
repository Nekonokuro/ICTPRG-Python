#Create a python program menu.py
#1.	Create a list food with the following items
#[Pizza,Pancake,Chips,Burgers, Pasta]
#2.	Display the list
#3.	Ask the user which item you would like to change 
#4.	Get the item’s index from the list ( use  index option for list)
#5.	Replace the item  with the new item. 
#6.	Display the list.

menu = ["Pizza", "Pancake", "Chips", "Burgers", "Pasta"]
user_change = input("Which item in menu you would like to add?\n")
index_1 = menu.index("Chips")
menu.remove("Chips")
menu.append(user_change)
print(menu)
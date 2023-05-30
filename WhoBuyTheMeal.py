# name = input("What is your name? ")

# print("my name is " + name)

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

list_len = len(names)
pay = random.randint(0, list_len - 1)
payee = names[pay]
print(f"{payee} is going to buy the meal today.")
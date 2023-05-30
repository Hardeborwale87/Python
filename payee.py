import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list_len = len(names)
pay = random.randint(0, list_len - 1)
payee = names[pay]
print(f"{payee} is going to buy the meal today.")

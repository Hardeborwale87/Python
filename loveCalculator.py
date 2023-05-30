print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

one = name1.lower()
two = name2.lower()
true = one.count('t') + two.count('t') + one.count('r') + two.count('r') + one.count('u') + two.count('u') + one.count('e') + two.count('e')
love = one.count('l') + two.count('l') + one.count('o') + two.count('o') + one.count('v') + two.count('v') + one.count('e') + two.count('e')
score = str(true) + str(love)
score = int(score)
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentor")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together")
else:
  print(f"Your score is {score}, not quite match")
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if your_choice >= 3:
    print("Check your selection again.")
else:
    you_select = choices[your_choice]
    print(you_select)

    # choice_lenght = len(choices)
    computer_choice = random.randint(0, 2)
    com_select = choices[computer_choice]
    print(f"\nComputer choose:\n {com_select}")

    if you_select == rock and com_select == paper:
        print("Computer won")
    elif you_select == com_select:
        print("Draw game")
    elif you_select == paper and com_select == rock:
        print("You won")
    elif you_select == paper and com_select == scissors:
        print("Computer won")
    elif you_select == scissors and com_select == paper:
        print("You won")
    elif you_select == scissors and com_select == rock:
        print("Computer won")
    elif you_select == rock and com_select == scissors:
        print("You won")
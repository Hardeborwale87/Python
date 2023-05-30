print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  # print("You can use the rollercoaster")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Children tickets are $5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
  elif age <= 22:
    bill = 12
    print("adult tickets are $12")

  want_photo = input("Do you want a photo taken? Y or N.")
  if want_photo ==  "Y":
    bill += 3
    print(f"Your bill is ${bill}")
  # else:
  #   print("Check your selection again. Y or N")
else:
  print("You have to grow some height to use the rollercoaster")
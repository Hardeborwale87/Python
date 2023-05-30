age = input("What is your current age?\n")

age = int(age)
days = 32850 - 356 * age
weeks = 4680 - 52 * age
months = 1080 - 12 * age
years = 90 - age

result = f"You have {days} days, {weeks} weeks, {months} months left, {years} years left."

print(result)
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip you would like to give? 10, 12, 15?"))

tip_percentage_result = tip_percentage / 100
percentage_amount = tip_percentage_result * total_bill
sharing_amount = percentage_amount + total_bill

num_of_people = int(input("How many people to split the bill?"))

bill_per_person = sharing_amount / num_of_people
# result = round(bill_per_person, 2)
result = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${result}")
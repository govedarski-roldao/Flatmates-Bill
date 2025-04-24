from flat import Bill, Flatmate
from reports import PdfReport

# Colect info regarding the names, total amount, days in the house
total_amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g December 2020: ")
name1 = input("What is your name? ")
name2 = input("What is your name? ")
name1_days_amount = int(input(f"How many days did {name1} stay in the house? "))
name2_days_amount = int(input(f"How many days did {name2} stay in the house? "))

# process the collected information with created classes
the_bill = Bill(total_amount, period)
first_mate = Flatmate(name1, name1_days_amount)
second_mate = Flatmate(name2, name2_days_amount)

# Print the total per flat mate in the console
print(f"{name1} pays", first_mate.pays(the_bill, second_mate))
print(f"{name2} pays", second_mate.pays(the_bill, first_mate))

# Create the report in PDF
generate = PdfReport("bills")
generate.generate(first_mate, second_mate, the_bill)

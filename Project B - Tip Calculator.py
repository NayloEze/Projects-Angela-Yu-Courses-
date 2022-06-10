## Tip Calculator

# Instructions

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill?")
tip_amount = input("How much tip would you like to give? 10, 12, or 15?")
number_of_people = input("How many people to split the bill?")

bill_tip = int(total_bill) * (1 + (int(tip_amount)/100))

total_individual_bill = (bill_tip / int(number_of_people))

print(f"Each person should pay: ${total_individual_bill: .2f}")
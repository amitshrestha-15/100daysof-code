print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill?  $"))
tip_per = int(input("What percentage tip would you like to give? 10, 12 , 15?"))
people = int(input("How many people to split the bill?"))

tip_amt = int(total_bill*(tip_per/100))
bill_with_tip = float(total_bill +tip_amt)
bill_per_person = bill_with_tip / people
final = "{:.2f}".format(bill_per_person)
print(f'Each person should pay: ${final}')

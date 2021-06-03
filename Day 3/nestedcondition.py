height = int(input("What is your height?\n"))
if height < 120:
    print("Sorry! You can't ride roller coster.")
else:
    age = int(input("What is your age?\n"))
    if age > 18:
        print("Ticket price is $12.")
    elif age < 12:
        print("Ticket price is $5")
    else:
        print("Ticket price is $7")
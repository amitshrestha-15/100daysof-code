print ("Welcome to roller coaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120 :
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket price is $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket price is $7.")
    elif age > 18 and age< 45:
        bill = 12
        print("Adult ticket price is $12.")
    elif age>= 45 and age <= 55:
        print("Your ride is free. But You should pay for photo.")
    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 3
    print(f"Your ticket price is ${bill}")
else:
    print("Sorry! You can't ride roller coaster.")
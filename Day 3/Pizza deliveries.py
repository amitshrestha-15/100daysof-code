print("Welcome to python PIZZA Deliveries!")
size = input("What size pizza do you want? S, M , or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra chees? Y or N ")
price = 0
pepperoni_add = 0
if size == "S":
    price = 15
    pepperoni_add = 2
    c_amt = 1
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is ${price+pepperoni_add+c_amt}")
        else:
            print(f"Your final bill is ${price+pepperoni_add}")
    else:
        print(f"Your final bill is ${price}")

elif size == "M":
    price += 20
    pepperoni_add = 3
    c_amt = 1
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is ${price+pepperoni_add+c_amt}")
        else:
            print(f"Your final bill is ${price+pepperoni_add}")
    else:
        print(f"Your final bill is ${price}")
elif size == "L":
    price += 25
    pepperoni_add = 3
    c_amt = 1
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is ${price+pepperoni_add+c_amt}")
        else:
            print(f"Your final bill is ${price+pepperoni_add}")
    else:
        print(f"Your final bill is ${price}")


import random

name_string = input("Give me everybody's name , separated by a comma.")
name = name_string.split(",")
random = int(random.randint(0, (len(name) - 1)))
print(f"{name[random]} is going to buy meal today.")

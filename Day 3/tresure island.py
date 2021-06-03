print("Welcome to Tresure Island.")
print("Your mission is to find the tresure.")
path = input("You are at a crossword, where do you want to go? Right or Left\n").lower()

if path == "left":
    choice_2 = input("You see another island. You want to wait for boat or swim across. 'wait' or 'swim'\n").lower()
    if choice_2 == "swim":
        print ("You are eaten by shark .Game OVer")
    if choice_2 == "wait":
        choice_3 = input("YOu arrive at the island.THere is 3 doors with color red, yellow, blue.Which do you choose?\n").lower()
        if choice_3 == "red":
            print("Game over.")
        elif choice_3 == "blue":
            print("YOu found tresure!")
        else:
            print("game over")
else:
    print("You fell into a hole.game over.")

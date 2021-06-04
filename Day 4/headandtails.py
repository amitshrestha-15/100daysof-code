import random
# random module imported
# toss as variable for tail and head
Toss = random.randint(0, 1)
if Toss == 1:
    print("Head")
else:
    print("Tail")

print("Welcome to the love calculator!")
name1 = input("What is boy's name?\n")
name2 = input("What is girl's name?\n")
combined = name1 + name2
lower = combined.lower()
t= lower.count("t")
r= lower.count("r")
u= lower.count("u")
e = lower.count("e")
true = t+r+u+e
l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

love = l+ o+ v+ e
love_score = 10*true + love
if love_score > 90 or love_score <10:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>= 40 and love_score<= 50:
    print(f"Your score is {love_score}, You are alright together.")
else:
    print(f"Your score is {love_score}")

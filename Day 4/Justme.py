print("Welcome to new world")
work_hr = input("How many hour did u code?  ")
study_hr = input("How many hour did u study?  ")
read_h = input("How many hour did u read?  ")
total_hour = int(work_hr) + int(study_hr) +int(read_h)
if total_hour <= 3:
    print("Bro try ahrd and think of your goals!")
elif total_hour>3 and total_hour<=6:
    print("GOing good. Make progress each day.")

elif total_hour >6 and total_hour <=8 :
    print("I am impressed bro you are grinding hard huh!")
else:
    print("Excessive of something ain't good.")
print("KEEP GOING KEEP TRYING HARD")

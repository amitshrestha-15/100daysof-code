# THIS IS BMI CALCULATOR
print("Welcome to BMI calculator!")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your height in kg: "))
bmi = weight/height**2
BMI = float("{:.2f}".format(bmi))
if BMI < 18.5:
    print("Your BMI is " + str(BMI) + ",your are underweight.")
elif 18.5 < BMI < 25 :
    print("Your BMI is " + str(BMI) + ",your are normal weight.")
elif 25 < BMI < 30 :
    print("Your BMI is " + str(BMI) + ",your are overweight.")
elif 30 < BMI < 35:
    print("Your BMI is " + str(BMI) + ",your are obese.")
else  BMI > 35:
    print("Your BMI is " + str(BMI) + ",your are clinically obese.")

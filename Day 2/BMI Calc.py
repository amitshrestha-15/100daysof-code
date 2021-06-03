height = float(input("Enter your height in 'm' :"))
weight = int(input("Enter your weight in 'kg' :"))
bmi = int((weight) / (height) ** 2)
print("BMI = " + str(round(bmi,0)))

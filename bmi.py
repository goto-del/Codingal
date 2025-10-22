weight = float(input("Engter your weight in kilograms: "))
height = float(input("Engter your height in meters: "))

bmi = weight / (height ** 2)
print("Your BMI is:"+ str(bmi))

if bmi < 18.5:
    print("You are underweight")
elif 18.6 <= bmi <= 24.9:
    print("You have a normal weight")
elif 25 <= bmi <= 29.9:
    print("You are overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("You are obese")
elif bmi >= 35:
    print("You are severely obese")
else:
    print("Invalid input")
weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

bmi = round((weight/(height ** 2)), 1)
print("Your bmi is", bmi)

if (bmi <= 18.5):
    print("You are underweight")
elif (bmi > 18.5 and bmi <= 24.9):
    print("You are normal weight")
elif (bmi > 24.9 and bmi <= 29.9):
    print("You are overweight")
else:
    print("You are obese")


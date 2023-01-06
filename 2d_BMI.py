print("BMI calculator")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

new_height = float(height)
new_weight = float(weight)

results = int((new_weight / (new_height**2)))

print(str(results) + " / (" + str(new_height) + " * " + str(new_height) + ") = " + str((new_weight/(new_height**2))))
if results < 18:
    print("Your BMI is " + str(results) + ", you are underweight.")
elif results > 18.5 and results < 25:
    print("Your BMI is " + str(results) + ", you have a normal weight.")
elif results > 25 and results < 30:
    print("Your BMI is " + str(results) + ", you are slightly overweight.")
elif results > 30 and results < 35:
    print("Your BMI is " + str(results) + ", you are obese")
else:
    print("Your BMI is " + str(results) + ", are clinically obese.")
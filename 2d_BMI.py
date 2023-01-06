print("BMI calculator")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

new_height = float(height)
new_weight = float(weight)

results = int((new_weight / (new_height**2)))
print(f"Your BMI is {results}")

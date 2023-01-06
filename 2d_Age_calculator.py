age = input("What is your current age? ")
new_age = (90 - int(age))

month = int(new_age * 12)
week = int(new_age * 52)
day = int(new_age * 365)

print(f"You have {day} days, {week} weeks, and {month} months left to 90 years.")

# Data Types
# String
"Hello"[0]  # wyświetlenie pierwszej listery - zawsze od zera

# Integer - numery bez żadnych dodatków

print((123) + (234))

# Float - typ danych po przecinku (Floten point number)

# Bolean (Trou lub False)

# num_char = len(input("What is your name?"))
# new_num_char=str(num_char)
# print("Your name has " + new_num_char + " characters.")

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

a = int(two_digit_number[0])
b = int(two_digit_number[1])

print(a+b)

#**** PEMDAS - kolejnośc wykonywania wyliczeń
#Parentheses ()
#Exponents **
#Multiplication *
#Division /
#Addition +
#Subtraction -
#****

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_height = float(height)
new_weight = float(weight)

results = (new_weight / (new_height**2))
print(int(results))

#8 // 2 - informuje o tym że jest to int
socer = 1
socer += 1
socer -= 2

f-stringf

f"your socer is {socre}"

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_age = (90 - int(age))

month = int(new_age * 12)
week = int(new_age * 52)
day = int(new_age * 365)

print(f"You have {day} days, {week} weeks, and {month} months left.")

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

Welcome = "Welcome to the tip calculator."
print(Welcome)

Bill = input("What was the totatl bill? $")

Tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
People = input("How many people to split the bill? ")

Tip_2 = ((float(Tip)) / 100)
Bill_2 = (float(Bill)) * Tip_2 + float(Bill)
People_2 = int(People)

suma = Bill_2 / People_2

reasult = round(suma,2)

print(f"Each person should pay: ${reasult}")
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to the tip calculator.")
Bill = float(input("What was the totatl bill? $"))
Tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
People = int(input("How many people to split the bill? "))
bill_with_tip = Tip / 100 * Bill + Bill
bill_per_person = bill_with_tip / People
final_amonut = round(bill_per_person)
final_amonut = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amonut}$")

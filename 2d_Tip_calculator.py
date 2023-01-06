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

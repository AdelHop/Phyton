print("Welcome to the tip calculator.")

Bill = float(input("What was the totatl bill? $"))
Tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
People = int(input("How many people to split the bill? "))

bill_with_tip = Tip / 100 * Bill + Bill
bill_per_person = bill_with_tip / People

final_amonut = round(bill_per_person)
final_amonut = "{:.2f}".format(bill_per_person)

print(f"Each person should pay {final_amonut}$")

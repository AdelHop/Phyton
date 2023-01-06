import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

suma = len(names)
losowanie = random.randint(0, suma -1)

print(names[losowanie] + " is going to buy the meal today!")
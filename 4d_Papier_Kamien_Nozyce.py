import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


liczba=input("Co wybierasz?\n 0 - Kamień\n 1 - Papier\n 2 - Nożyczki\n")

znak = int(liczba)
znak2 = random.randint(0, 2)

if znak == 0:
    print(rock)
elif znak == 1:
    print(paper)
else:
    print(scissors)

if znak2 == 0:
    print("Komputer wybiera:\n" + rock)
elif znak2 == 1:
    print("Komputer wybiera:\n" + paper)
else:
    print("Komputer wybiera:\n" + scissors)

wynik = str(znak) + str(znak2)

if wynik == "00" or wynik == "11" or wynik == "22":
    print("Spróbuj ponownie")
elif wynik == "10" or wynik == "02" or wynik == "21":
    print("Wygrałeś!")
else:
    print("Komputer wygrał!")
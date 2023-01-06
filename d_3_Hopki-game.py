# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Witam w świecie Hopków")
# print("Twoim zadaniam jest odgadnięcie wszystkich członków rodziny.")
# print("Powodzenia")
#
# #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#
# #Write your code below this line 👇
#
# rodzina = input("Z ilu członków składa się rodzina Hopków 2 / 3 / 4 / 5?\n")
#
# if rodzina == "4":
#     dzieci = input("Ile jest dzieci u Hopków?\n").lower()
#     if dzieci == "2":
#         Ewa = input("Ile ma najstarsza córka Hopków?\n").lower()
#         if Ewa == "4":
#             Ewa2 = input("Jak ma na imię najstarsza córka Hopków?\n").lower()
#             if Ewa2 == "ewa":
#                 Iza = input("Jakiej półci jest 2 dziecko? Chłopiec czy dziewczynka \n").lower()
#                 if Iza == "dziewczynka":
#                     Iza2 = input("W którym roku urodziła się Iza?\n").lower()
#                     if Iza2 == "2020":
#                         zwierze = input("Czy Hopki mają zwierzęta? Y/N \n").lower()
#                         if zwierze == "Y".lower():
#                             print("Znasz Hopków i Dizla. BRAWO")
#                         else:
#                             print("Paweł, Dizel jest nadal naszym psem :)")
#                     else:
#                         print("Iza urodziła się 2020, sprobuj jeszcze raz.")
#                 else:
#                     print("To dziewczynka! Spróbuj jeszcze raz.")
#             else:
#                 print("Ma na imię Ewa, spróbuj jeszcze raz.")
#         else:
#             print("Ma 4 lata, spróbuj jeszcze raz.")
#     else:
#         print("Niestety nieznasz Hopków. Spróbuj jeszcze raz.")
# else:
#     print("Niestety nieznasz Hopków - jest ich 4. Lepiej odpuść")
# #
#

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
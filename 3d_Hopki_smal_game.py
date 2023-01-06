print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Witam w świecie Hopków")
print("Twoim zadaniam jest odgadnięcie wszystkich członków rodziny.")
print("Powodzenia")

rodzina = input("Z ilu członków składa się rodzina Hopków 2 / 3 / 4 / 5?\n")

if rodzina == "4":
    dzieci = input("Ile jest dzieci u Hopków?\n").lower()
    if dzieci == "2":
        Ewa = input("Ile ma najstarsza córka Hopków?\n").lower()
        if Ewa == "4":
            Ewa2 = input("Jak ma na imię najstarsza córka Hopków?\n").lower()
            if Ewa2 == "ewa":
                Iza = input("Jakiej półci jest 2 dziecko? Chłopiec czy dziewczynka \n").lower()
                if Iza == "dziewczynka":
                    Iza2 = input("W którym roku urodziła się Iza?\n").lower()
                    if Iza2 == "2020":
                        zwierze = input("Czy Hopki mają zwierzęta? Y/N \n").lower()
                        if zwierze == "Y".lower():
                            print("Znasz Hopków i Dizla. BRAWO")
                        else:
                            print("Paweł, Dizel jest nadal naszym psem :)")
                    else:
                        print("Iza urodziła się 2020, sprobuj jeszcze raz.")
                else:
                    print("To dziewczynka! Spróbuj jeszcze raz.")
            else:
                print("Ma na imię Ewa, spróbuj jeszcze raz.")
        else:
            print("Ma 4 lata, spróbuj jeszcze raz.")
    else:
        print("Niestety nieznasz Hopków. Spróbuj jeszcze raz.")
else:
    print("Niestety nieznasz Hopków - jest ich 4. Lepiej odpuść")
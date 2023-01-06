# # # # import random
# # # # import my_module

# # # # random_integer = random.randint(1, 10)
# # # # print(random_integer)

# # # '''Wypisz liczby z z zakresu 0.00000000 do 0,999999999...'''
# # # # random_float = random.random()

# # # # print(random_float)

# # # '''Wypisz liczby z zakresu 1 do 5'''

# # # # random_integer = random.randint(1, 5)
# # # # print(random_integer)

# # # '''Wypisz liczby z zakresu 0.00000 do 5'''

# # # # random_float = random.random()

# # # # print(random_float *5)

# # # # state_of_america =["Delewer", "Pennsylvenia"]



# # # random_choice = random.choice(names)
# # # print(random_choice)

# # # 🚨 Don't change the code below 👇
# # row1 = ["⬜️","️⬜️","️⬜️"]
# # row2 = ["⬜️","⬜️","️⬜️"]
# # row3 = ["⬜️️","⬜️️","⬜️️"]
# # map = [row1, row2, row3]
# # print(f"{row1}\n{row2}\n{row3}")
# # position = input("Where do you want to put the treasure? ")
# # # 🚨 Don't change the code above 👆

# # #Write your code below this row 👇

# # position2 = int(position)
# # if position2 == 11:
# #     row1[0]= "X"
# # if position2 == 12:
# #     row2[0]= "X"
# # if position2 == 13:
# #     row3[0]= "X"
# # if position2 == 21:
# #     row1[1]= "X"
# # if position2 == 22:
# #     row2[1]= "X"
# # if position2 == 23:
# #     row1[1]= "X"
# # if position2 == 31:
# #     row1[2]= "X"
# # if position2 == 32:
# #     row2[2]= "X"
# # if position2 == 33:
# #     row3[2]= "X"

# # #Write your code above this row 👆

# # # 🚨 Don't change the code below 👇
# # print(f"{row1}\n{row2}\n{row3}")

# # # 🚨 Don't change the code below 👇
# # row1 = ["⬜️","️⬜️","️⬜️"]
# # row2 = ["⬜️","⬜️","️⬜️"]
# # row3 = ["⬜️️","⬜️️","⬜️️"]
# # map = [row1, row2, row3]
# # print(f"{row1}\n{row2}\n{row3}")
# # position = input("Where do you want to put the treasure? ")
# # # 🚨 Don't change the code above 👆

# # #Write your code below this row 👇

# # horizonal = int(position[0])
# # vertical = int(position[1])

# # selected_row = map[vertical - 1]
# # selected_row[horizonal - 1] = "X"

# # #Write your code above this row 👆

# # # 🚨 Don't change the code below 👇
# # print(f"{row1}\n{row2}\n{row3}")
# '''Albo # map[vertical - 1][horizonal - 1] = "X" '''

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''


# liczba=input("Co wybierasz?\n 0 - Kamień\n 1 - Papier\n 2 - Nożyczki\n")

# znak = int(liczba)
# znak2 = random.randint(0, 2)

# if znak == 0:
#     print(rock)
# elif znak == 1:
#     print(paper)
# else:
#     print(scissors)

# if znak2 == 0:
#     print("Komputer wybiera:\n" + rock)
# elif znak2 == 1:
#     print("Komputer wybiera:\n" + paper)
# else:
#     print("Komputer wybiera:\n" + scissors)

# wynik = str(znak) + str(znak2)

# if wynik == "00" or wynik == "11" or wynik == "22":
#     print("Spróbuj ponownie")
# elif wynik == "10" or wynik == "02" or wynik == "21":
#     print("Wygrałeś!")
# else:
#     print("Komputer wygrał!")

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
game_images = [rock, paper, scissors]
user_choice = int(input("Co wybierasz?\n 0 - Kamień\n 1 - Papier\n 2 - Nożyczki\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer choice:{game_images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice == user_choice:
        print("It's draw")
    else:
        print("You typed an invalid number, you lose!")




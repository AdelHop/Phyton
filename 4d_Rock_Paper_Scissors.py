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
user_choice = int(input("What your choose?\n 0 - Rock\n 1 - Paper\n 2 - Scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

else:
    computer_choice = random.randint(0, 2)
    print(f"Computer choice:{game_images[computer_choice]}")
    result = str(user_choice) + str(computer_choice)
    if result == "00" or result == "11" or result == "22":
        print("Try again!")
    elif result == "10" or result == "02" or result == "21":
        print("You win!")
    elif result == "01" or result == "20" or result == "12":
        print("You lose.")
    else:
        print("You typed an invalid number, you lose!")

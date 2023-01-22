import random
import Hangman_List

chosen_world = random.choice(Hangman_List.word_list)
from Hangman_logo import logo
from Hangman_logo import stages

print('Witam w grze "Wisielec". Odgadnij nazwe wylosowanego województwa.')
print(chosen_world)

display = []
for _ in range(len(chosen_world)):
    display += "_"

print(display)
lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Wybierz litere: ").lower()
    if guess not in chosen_world:
        lives -= 1
        print(f"Wybrałeś literę {guess}, nie wytępuje ona w wylosowanej nazwie. Straciłeś jedno życie.")
        print(stages[lives])

    for position in range(len(chosen_world)):
        letter = chosen_world[position]
        # print(f"Current position: {position}\n Current letter:{letter}\n Guessed letter: {guess}")
        if display[position] == guess:
            print("Już wskazałeś tą literę wcześniej.")

        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        ens_of_game = True
        print("Wygrałeś")

    elif lives == 0:
        end_of_game = True
        print("Przegrałeś")






    # display2 = []
    # for position in range(len(chosen_world)):
    #     letter = chosen_world[position]
    #     if letter == guess:
    #         display[position] = letter

# for letter in chosen_world:
#   if letter != guess:
#       display2 += "_"
#
#   else:
#       display2 += guess
#
# print(display2)

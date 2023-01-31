import random

logo = """ do wstawienia """
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start = 'y'
"""input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")"""
print(start)
user_card = []
user_s = []
computer_card = []
computer_s = []

def start_bj():
    print(logo)
    user_card.append(random.choice(cards))
    user_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))
    user_s.append(user_score(user_card))
    print(f"Your cards: {user_card}, current score: {user_s}")
    print(f"Computer's first card: {computer_card}")
    print("Type 'y' to get anather card, type 'n' to pass:")

def user_score(v_user_card):
    return sum(user_card)

if start == "y":
    start_bj()




# elif start == "n":
#
# else:
#     print("Write good answer")

"""
1. "Do you want to play a game of Blackjack? Type 'y' or 'n': "
2.  logo 

    Your cards: [6,2], current score: 8
    Computer's first card: 3
Type 'y' to get anather card, type 'n' to pass:

3.  Your cards: [6,2,10], current score: 18
    Computer's first card: 3
    Type 'y' to get anather card, type 'n' to pass:

4. Wybrałam "n" 
    Your final hand: [6,2,10], final score: 18
    Computer's final hand:[3, 2, 4, 10], final score: 19
You lose :(
Do you want to play a game of Blackjack? Type 'y' or 'n': "
   
5. N - kończy grę - nic nie jest napisane Y zaczyna od nowa 


"""
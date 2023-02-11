import random

logo = """ do wstawienia """
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start = 'y'
"""input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")"""
user_card = []
user_s = []
user_c = []
user_sc = []
computer_card = []
computer_s = []
contin = []
def computer_score(v_computer_score):
    return sum(computer_card)
def user_score(v_user_c):
    user_c = [int(item) for item in user_card]
    return sum(user_c)

"START"

print(logo)
user_s = []
start = 'n'
user_card.append(random.choice(cards))
user_card.append(random.choice(cards))
computer_card.append(random.choice(cards))
user_s.append(user_score(user_c))
print(f"Your cards: {user_card}, current score: {user_s}")
print(f"Computer's first card: {computer_card}")

user_s = []
user_card.append(random.choice(cards))
user_s.append(user_score(user_c))
user_sc = [int(item) for item in user_s]
print(type(user_sc))
#
# if user_sc > 21:
#     print("You lose :(")
#     start = (input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
#
# elif user_sc < 21:
#     contin = input("Type 'y' to get anather card, type 'n' to pass: ")
#     if contin == "y":
#         print("bład")
#
#     elif contin == "n":
#         if computer_s < 18:
#            computer_card.append(random.choice(cards))
#            computer_s.append(computer_score(computer_card))
#         elif computer_s > 18 and computer_card < 21:
#            print(f"Your cards: {user_card}, current score: {user_s}")
#            print(f"Computer's final hand:{computer_card}, final score: {computer_s}")
#            print("Computer win")

# if(start):
#     start_bj(user_card, user_s, computer_score, computer_card, computer_s, contin, start, user_sc)
#     contin = input("Type 'y' to get anather card, type 'n' to pass: ")

    # while contin == 'y':
    #     continue_2(user_card,computer_score)
    #     contin = input("Type 'y' to get anather card, type 'n' to pass: ")

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
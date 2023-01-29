# Funkcja pozwalająca na ukrycie danych poprzedniego użytkownika
import os
import auction_logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

users = []
other_users = "Yes"

def add_new_user(name2, bid2, users):
    new_user = {}
    new_user["name"] = name2
    new_user["bid"] = bid2
    users.append(new_user)

while other_users == "Yes":
        name = input("What's your name? ")
        bid = input("What's your bid ")
        add_new_user(name2=name,bid2=bid,users=users)
        other_users = input("Are there other users? Yes / No ")

else:
    userMax = users[0]
    for user in users:
        if int(user["bid"]) > int(userMax["bid"]):
            userMax = user

print(f'The winer is {userMax["name"]} with a bid of ${userMax["bid"]}.')
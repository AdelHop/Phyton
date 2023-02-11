import random
import Higher_lower_game_data
import Higher_lower_art

print(Higher_lower_art.logo)

List = Higher_lower_game_data.data
Score = 0
Answer = []
Start = True

def choiceMan():
    return random.choice(List)

def followers(man):
    return int(man['follower_count'])

def printMan(man, name):
    print((f"{name}: {man['name']}, a {man['description']}, from {man['country']}. psst... {man['follower_count']}"))

while Start == True:

    manA = choiceMan()
    manB = choiceMan()
    while followers(manA) == followers(manB):
        manB = choiceMan()

    printMan(manA, "Compare A")
    print(Higher_lower_art.vs)
    printMan(manB, "Against B")
    Answer = (input("Who has more followers? Type 'A' or 'B': "))

    if followers(manA)>followers(manB):
        CorrectAnswer = "A"
    else:
        CorrectAnswer = "B"

    if Answer == CorrectAnswer:
        Score += 1
        print(f"You're right! Current score: {Score}")
    else:
        print(f"Sorry, that's wrong. Final score: {Score}")
        Start = False
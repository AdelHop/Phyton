import random

logo = """ wstaw """

draw = random.randint(1, 100)

def Start(draw):
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # print(f"Pssst, the correct answer is {draw} draw")

def Guess(draw, turns):

    while True:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if turns > 0:
            turns -= 1
            if guess < draw:
                print("Too low.")
            elif guess > draw:
                print("Too high.")
            else:
                print("You win.")
                return False
        elif turns == 0:
            print("You lose.")
            exit()

def Difficult():
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
        return 10
    else:
        return 5


Start(draw)
turns = Difficult()
Guess(draw,turns)




# ("Too low.")
#
# ("Too high.")


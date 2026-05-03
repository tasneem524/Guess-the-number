import random

def play():
    number=random.randint(1,100)
    lives=7

    print("Welcome to the guess the number game!")
    print("I have selected a number between 1 to 100.can you guess it?")
    print(f"you have {lives} lives to guess the number correctly.")

    while lives>0:
        guess=int(input("Enter a number betweeen 1 to 100:"))
        if guess==number:
            print(f"Congratulations! You guessed the number correctly.")
            return
        elif guess<number:
            diff=number-guess
            if diff<=10:
                print("You're very close!")
            else:
                print("Too low! Try again.")
        else:
            diff=guess-number
            if diff<=10:
                print("You're very close!")
            else:
                print("Too high! Try again.")
        lives-=1
    print("game over!")
    print(f"Sorry, you ran out of lives. The number was {number}.")

while True:
    play()
    if input("Do you want to play again (yes/no)? ").lower() != "yes":
        break
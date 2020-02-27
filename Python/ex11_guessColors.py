import random

colors = ["yellow", "red", "blue", "green", "gray", "white", "black", "pink", "brown"]

while True:
    userContinue = input("Do you want to play? ")
    if userContinue.lower() == "no":
        break
    else:
        randColor = colors[random.randint(0, len(colors))]
        guess = input("Guess a color: ")
        while True:
            if guess.lower() == randColor:
                break
            else:
                guess = input("Wrong, try again: "))

        print("You guessed right, the color is:", randColor)

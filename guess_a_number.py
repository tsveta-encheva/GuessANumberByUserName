import random

computer_number = random.randint(1,100)

while True:
    player_input = input("Guess the number: ")

    if not player_input.isdigit():
        print("Invalid input! Try againn...")

    player_number = int(player_input)

    if player_number == computer_number:
        print("You guess it!")
        break

    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")
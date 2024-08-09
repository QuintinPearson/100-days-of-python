print("Welcome to Treasure Island.\nYour mission is to find the treasure")


# Initialize game
def game():
    choice = input("To continue choose to go 'left' or 'right'.\n").lower()

    while choice != "left" and choice != "right":
        choice = input("To continue choose to go 'left' or 'right'.\n")

    # First Level
    if choice != "left":
        return print("game over")
    else:
        choice = input("'swim' or 'wait'?\n").lower()

    # Second Level
    if choice != "wait":
        return print("Game over! Shark ate you :(")
    else:
        choice = input("'red', 'yellow' or 'blue' door?\n").lower()

    # Third Level
    if choice == "red" or choice == "yellow":
        return print("Game Over!!")
    elif choice == "blue":
        return print("YOU WIN!!")
    else:
        return print("You suck!")
    

game()
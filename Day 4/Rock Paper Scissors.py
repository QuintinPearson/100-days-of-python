# Create a rock paper scissors game using Python

# Import Random
import random

# Set Options and Scores Variables
options = ["Rock", "Paper", "Scissors"]
scores = {
    "your_score": 0,
    "computer_score": 0
}

# Set Variable to determine whether the game should continue
game_over = False

while not game_over:
    # Print scores each time
    print("#########################################")
    print(f"You: {scores['your_score']}\nComputer: {scores['computer_score']}")

    # Ask user Choice and loop if invalid

    choice = int(input("What do you choose? Type '0' for Rock '1' for Paper and '2' for Scissors.\n"))

    while choice < 0 or choice > 2:
        choice = int(input("What do you choose? Type '0' for Rock '1' for Paper and '2' for Scissors.\n"))

    # Set PC Choice
    computer_choice = random.randint(0, 2)

    # Print Choices

    print(f"You Chose {options[choice]}")
    print(f"Computer Chose {options[computer_choice]}")

    # Print whether you or PC wins and add scores

    if choice == computer_choice:
        print("It's a draw\n")    
    elif choice == 0 and computer_choice == 2:
        scores["your_score"] += 1
        print("You Win!\n")
    elif choice == 1 and computer_choice == 0:
        scores["your_score"] += 1
        print("You Win!\n")
    elif choice == 2 and computer_choice == 1:
        scores["your_score"] += 1
        print("You Win!\n")
    else:
        scores["computer_score"] += 1
        print("Computer Wins :(\n")

    # Check if any score is more than 2 and End Game if so

    if scores["computer_score"] > 2:
        print(f"Computer has {scores['computer_score']} and you have {scores['your_score']}, Computer Wins!")
        game_over = True
    elif scores["your_score"] > 2:
        print(f"Computer has {scores['computer_score']} and you have {scores['your_score']}, You Win!")
        game_over = True

    print("#########################################")
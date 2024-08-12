import random

game_over = False




# Set the scores
scores = {
    "your_score": 0,
    "computer_score": 0
}

# Set the Options
options = ["Rock", "Paper", "Scissors"]

# Use functions to improve readability, maintenance and re-use

# Get the Users choice [Use a try catch to prevent chars from working and only allow numbers between 0-2]
def get_choice():
    while True:
        try:
            choice = int(input("What do you choose? Type '0' for Rock '1' for Paper and '2' for Scissors.\n"))
            if 0 <= choice <= 2:
                return choice
            else:
                print("Please enter a valid number")

        except ValueError:
            print("Invalid Input, Please enter a number")



# Get Computer Choice
def get_computer_choice():
    return random.randint(0, 2)


# Find Winner
def find_winner(choice, computer_choice, scores):
    # Set The winning conditions
    winning_conditions = {
        0: 2, # Rock beats Scissors
        1: 0, # Paper Beats Rock
        2: 1  # Scissors beats Paper
    }
    # work out the logic
    if choice == computer_choice:
        print("It's a draw\n")
    elif winning_conditions[choice] == computer_choice:
        scores["your_score"] += 1
        print("You Win!\n")
    else:
        scores["computer_score"] += 1
        print("You Lose!\n")

# Print The Scores
def print_scores(scores):
    print(f"You: {scores['your_score']}\nComputer: {scores['computer_score']}.")

# Create a function to reset scores
def reset_scores(scores):
    for key in scores:
        scores[key] = 0



# Main Game Loop, where we use the functions

while not game_over:
    print_scores(scores)

    choice = get_choice()

    computer_choice = get_computer_choice()

    print(f"You Chose: {options[choice]}")
    print(f"Computer Chose: {options[computer_choice]}")

    # Find a winner
    find_winner(choice, computer_choice, scores)

    # Check if anyone has reached 3
    if scores["computer_score"] > 2 or scores["your_score"] > 2:
        winner = "You Win! The Game" if scores["your_score"] > scores["computer_score"] else "You Lose The Game!"
        print(f"{winner} Final Score: You: {scores['your_score']} Computer: {scores['computer_score']}")

        # Ask To Play Again
        play_again = input("Do You want to play again? (yes/no): ").lower()
        if play_again != "yes":
            game_over = True
        else:
            reset_scores(scores)
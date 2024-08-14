# Imports are always at the top of the file
import random

# Create all the functions at the top to better separate functions from the main game

# Function to import words from the words.txt file
def load_words(file_path):
    """
    Load a list of words from a text file, each word on a new line.

    Args:
        file_path (str): The path to the file containing the words.

    Returns:
        list: A list of words read from the file.

    Example:
        words = load_words('words.txt')
    """
    with open(file_path, "r") as file:
        words = file.read().splitlines()
        return words

# Function to Chose a word  
def choose_word(words):
    """
    Returns a single word from a list of words.

    Args:
        words (list): the list of words you want to extract a random word from.

    Retruns: 
        word: a single word

    Example:
        chosen_word = choose_word(words)
    """
    chosen_word = random.choice(words)
    return chosen_word

# Function to Scramble the word
def scramble_word(word):
    """
    Returns a scrambled word.

    Args:
        word (str): A single word you want scrambled.

    Returns:
        word: a scrambled word

    Example:
        scrambled_word = scramble_word(chosen_word)
    """

    return "".join(random.sample(word, len(word)))

# A function to check if the guess is correct
def check_guess(guess, original):
    """
    Compares the guess to the original chosen word.

    Args:
        guess (str): The users guess
        original (str): The original word

    Returns:
        bool: True or False

    Example:
        correct_guess = check_guess(guess, chosen_word)
        if correct_guess:
            print("You're right!")
        else:
            print("Try Agian!")

    """
    if guess.lower() == original.lower():
        return True
    else:
        return False
    
# Function to Update the score
def update_score(current_score, correct_guess):
    """
    Updates the score depending on a correct guess.

    Args:
        current_score (int): The players current score
        correct_guess (bool): Whether the guess was correct or not.

    Returns:
        int: Updated score

    Example:
        score = update_score(score, correct_guess)
    """
    if correct_guess:
        current_score += 1
    return current_score
    
# Set variables
score = 0

# Create a while looop to have the game continue for 3 rounds
while score < 3:
    # Step 1: Initialize a list of words to choose from   
    words = load_words("words.txt")

    # Step 2: Randomly select a word from the list to scramble
    chosen_word = choose_word(words)

    # Step 3: Scramble the selected word
    scrambled_word = scramble_word(chosen_word)


    # Step 4: Present the scrambled word to the user
    print(f"Your word for this round is {scrambled_word}")

    # Step 5: Prompt the user to guess the original word
    guess = input("What do you think the word is?\n").lower()

    # Step 6: Check if the user's guess is correct
        # If correct, congratulate the user and end the game
        # If incorrect, provide feedback and allow the user to guess again
    correct_guess = check_guess(guess, chosen_word)
    if correct_guess:
        print("You're Right!")
    else:
        print(f"try again:( The word was {chosen_word}")

    # Step 7: Track the number of attempts and consider providing hints after a few incorrect guesses (optional)
    score = update_score(score, correct_guess)
    print(f"Your score is: {score}")
    print("###############################################################")

    # Step 8: After the score =, ask if the user wants to play again
    if score == 3:
        continue_game = input("Do you want to play again? (Yes/No)\n")
        if continue_game.lower() == "yes":
            score = 0
        else:
            break

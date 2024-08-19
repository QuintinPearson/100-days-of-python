from words import words
import random
import hangman_art


# Set Variables
incorrect_guesses = 0
game_over = False
current_art = len(hangman_art.stages) - 1


# Functions

# Function to randomly choose a word
def choose_word(words):
    """
    Returns a single word from a list of words

    Args: 
        words (list): a list of words to choose from

    Returns: 
        word (str): a single word

    Example: 
        chosen_word = choose_word(words)

    """
    return random.choice(words).lower()

# Function to mask the word
def mask_word(word):
    """
    Returns a masked version of a word

    Args: 
        word (str): a single word to be masked

    Returns: 
        word (str): a single masked word

    Example: 
        masked_word = mask_word(word)

    """
    masked_version = ""
    for _ in range(len(word)):
        masked_version += "_"

    return masked_version

# Function to check a guess
def check_guess(guess, original_word):
    return guess in original_word

# Function to replace correct guesses in masked word
def replace_mask(guess, masked_word, chosen_word):
    chosen_arr = list(chosen_word)
    masked_arr = list(masked_word)

    for i, char in enumerate(chosen_arr):
        if guess == char:
            masked_arr[i] = guess

    return "".join(masked_arr)

# Function to check if the word is completed

def check_complete(masked_word):
    if "_" in masked_word:
        return False
    return True

# Function to increase increase incorrect guesses
def add_incorrect_guess(amount):
    amount += 1
    return amount


print(hangman_art.logo)
# Generate a random word
chosen_word = choose_word(words)

# Mask the word
masked_word = mask_word(chosen_word)

while not game_over:

    print(hangman_art.stages[current_art])
    print(f"You have {current_art} guesses left")
    print(masked_word)
    print(f"incorrect guesses = {incorrect_guesses}")



    # Prompt a Guess from the user
    while True:
        guess = input("Guess a letter in the word\n").lower()
        if len(guess) == 1 and guess.isalpha():
            break
        print("please enter a single letter.")

    # Check guess agains original word
    correct_guess = check_guess(guess, chosen_word)


    # Check if correct or incorrect
    if correct_guess:
        # If correct guess - Replace the mask at letter
        masked_word = replace_mask(guess, masked_word, chosen_word)
        print(masked_word)

        # If Incorrect guess - Draw a feature
    elif not correct_guess:
        incorrect_guesses = add_incorrect_guess(incorrect_guesses)
        current_art = (len(hangman_art.stages) - incorrect_guesses) - 1

    # Check if word is solved
    is_solved = check_complete(masked_word)
    if is_solved:
        print("You Win!")
        game_over = True

    # check if all guesses are used
    elif current_art < 1:
        print(hangman_art.stages[current_art])
        print("You Lose!")
        print(f"The correct word was: '{chosen_word}'")
        game_over = True

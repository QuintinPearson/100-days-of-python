import random

# Arrays for different character types
numbers = list('0123456789')
symbols = list('!@#$%^&*()-_=+[]{}|;:,.<>?/~`')
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

# Create a function that creates the password
def generate_password(num_amount, symbols_amount, letters_amount):
    password_array = []

    # Get Numbers
    for _ in range(num_amount):
        password_array.append(random.choice(numbers))
    # Get Symbols
    for _ in range(symbols_amount):
        password_array.append(random.choice(symbols))
    # Get Letters
    for _ in range(letters_amount):
        password_array.append(random.choice(letters))

    random.shuffle(password_array)

    return "".join(password_array)


num_amount = int(input("How many Numbers do you want in your password?\n"))
symbols_amount = int(input("How many Symbols do you want in your password?\n"))
letters_amount = int(input("How many letters do you want in your password?\n"))


password = generate_password(num_amount, symbols_amount, letters_amount)

print(password)
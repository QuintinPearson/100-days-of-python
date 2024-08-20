import string


def get_choice():
    while True:
        choice = input("Type 'encode' to encrypt or 'decode' to decrypt\n").lower()
        try:
            if choice not in ['encode', 'decode']:
                raise ValueError("Please choose either 'encode' or 'decode'")
            return choice
        except ValueError as e:
            print(e)
            print("Let's try again")


def get_string():
    while True:
        user_string = input("Please enter your string.\n").lower()
        try:
            if user_string == "" or not user_string.replace(" ","").isalpha():
                raise ValueError("Please enter a valid string")
            return user_string
        except ValueError as e:
            print(e)
            print("Please try again")


def get_offset():
    while True:
        amount = input("Please choose an offset.\n")
        try:
            user_int = int(amount)
            return user_int
        except ValueError:
            print("You entered an invalid number")


def handle_string(string, offset, alphabet):
    result = ""
    for letter in string:
        if letter == " ":
            result += " "
        else:            
            index = alphabet.index(letter)
            new_index = index + offset
            result += alphabet[new_index]
    return result

        




def get_lowercase_alphabet():
    return list(string.ascii_lowercase)

def main():
    while True:

        # Ask User which they want to do
        choice = get_choice()

        # Ask for a string to handle
        string_to_handle = get_string()

        # Ask user for an offset
        offset = get_offset()

        # set the alphabet list
        alphabet = get_lowercase_alphabet()

        if choice == "encode":
            result = handle_string(string_to_handle, offset, alphabet)
        elif choice == "decode":
            result = handle_string(string_to_handle, -offset, alphabet)

        print(f"Here's your {choice}d string\n{result}")

        # Ask to continue
        while True:
                
            end_app = input("Do you want to continue? y/n\n").lower()
            if end_app == "n":
                return
            elif end_app == "y":
                break
            else:
                print("Please enter 'y' or 'n'.")



main()
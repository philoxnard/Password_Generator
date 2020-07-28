# Password Generator
# 7/28/2020

# A program to generate random passwords for different accounts and websites
# Once generated, it will store the password in a text document

###########################################################

# Imports for the program

import random

# Standard variables for the program

# These are the lists of characters that the password can contain
alphabet = "abcdefghijklmnopqrstuvwxyz"
characters = "!@#$%^&*()?"
digits = "1234567890"

# Create an empty list that will fill up as the password is created
password = []

# This is the file that the password info will be written to
filename = "passwords.txt"

############################################################

# Functions for the program

# Function to get the desired password length from the user
def get_password_length():
    password_length_check = 0
    while password_length_check == 0:
        password_length = input("\nHow many characters should the password be? ")
        if password_length.isdigit():
            if int(password_length) > 7:
                password_length_check = 1
                return int(password_length)
            else: print("Error, password must be at least 8 characters.\n")
        else:
            print("Error, please enter a number\n")
    

# Function to generate the random password as a list
def get_password(password_length):
    for i in range(0, password_length):
        random_character = random.randint(0, 3)
        if random_character == 0:
            password.append(alphabet[random.randint(0, len(alphabet) - 1)])
        if random_character == 3:
            password.append(alphabet[random.randint(0, len(alphabet) - 1)].upper())
        if random_character == 1:
            password.append(characters[random.randint(0, len(characters) - 1)])
        if random_character == 2:
            password.append(digits[random.randint(0, len(digits) - 1)])
    return password

# Function to display the password as a neatly formatted string
def display_password(password):
    print()
    password_string = ""
    for i in password:
        password_string += i
    print("Your password is: " + password_string)
    return password_string

# Prompts the user for the name of the account/website the password is for
def get_account_name():
    print("What website or account is this password for?")
    print("This information will be saved along with the generated password in a text file.")
    account = input()
    return account

# Prompts the user for their desired username
def get_username():
    print("\nWhat will be your username for this website?")
    username = input()
    return username

# Saves the user info to a separate document
def save_password(account, username, password):
    with open(filename, "a") as f_obj:
        f_obj.write("\nWebsite/Account: " + account.title())
        f_obj.write("\nUsername: " + username)
        f_obj.write("\nPassword: " + password)
        f_obj.write("\n_____________________________________________")
    print("Your password has been saved to " + filename)

############################################################################3

# Function that contains the higher level logic of the program
def main():
    account = get_account_name()
    username = get_username()
    password_length = get_password_length()
    password = get_password(password_length)
    password = display_password(password)
    save_password(account, username, password)

# Actual program code
main()

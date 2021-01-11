"""
This program will allow user to play the game hangman! The program will store a
predetermined list of secret words, and generate a random one the user must
guess. User must repeatedly guess single letters that might be in the word until
they've guessed all the letters in the word or run out of guesses and thus
the man is hung.
"""

import random
import sys

# Create list of possible words for secret_word
words = ["mystique", "nature", "light", "darkness", "determination", "pencil"]

# Assign secret_word at random from list
secret_word = random.choice(words)

# Assign dashes based on length of secret word
dashes = "-" * len(secret_word)

# Set initial value of how many guesses user has to 10
guesses_left = 10

# Initiate list of letters user has guessed to avoid repeated guessing
previous_guesses = []

# This function continues to retrieve a guess from user as long as user's guess 
# is not a single lowercase letter and user have not guessed it before.
def get_guess():
    while True:
        guess = input("Guess: ")
        if not isinstance(guess, str):
            print("Your guess must be a string consisting of one letter!")
        elif not guess.isalpha():
            print("Your guess must be an alphabetical letter!")
        elif len(guess) > 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        elif guess in previous_guesses:
            print("You've already guessed this letter!")
        else:
            previous_guesses.append(guess)
            if guess in secret_word:
                print("That letter is in the secret word!")
                return guess
            else:
                print("That letter is not in the secret word!")
                return guess
            break

# This function takes user's guess and updates "dashes" with all instances of
# user's guess appearing in "dashes" in the right places
def update_dashes(secret_word, dashes, guess):
    dashes = list(dashes)
    for i in range(len(dashes)):
        # If a letter of the secret_word matches user's guess, update dashes
        if secret_word[i] == guess:
            dashes[i] = guess
    dashes = ("").join(dashes)
    return dashes

# These 10 functions print the progression of the hangman picture
def print_hang_stand():
    print("      _______")
    print("     |       |")
    for i in range(8):
        print("     |")
    print("_____|_______")

def print_head():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    for i in range(6):
        print("     |")
    print("_____|_______")

def print_torso():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    for i in range(3):
        print("     |      |")
    for i in range(3):
        print("     |")
    print("_____|_______")

def print_arm1():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    print("     |      |")
    print("     |     \|")
    print("     |      |")
    for i in range(3):
        print("     |")
    print("_____|_______")

def print_arm2():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    print("     |      |")
    print("     |     \|/")
    print("     |      |")
    for i in range(3):
        print("     |")
    print("_____|_______")

def print_leg1():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    print("     |      |")
    print("     |     \|/")
    print("     |      |")
    print("     |     /")
    print("     |    /")
    print("     |")
    print("_____|_______")
    
def print_leg2():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    print("     |      |")
    print("     |     \|/")
    print("     |      |")
    print("     |     / \\")
    print("     |    /   \\")
    print("     |")
    print("_____|_______")

def print_hand1():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    print("     |    _ |")
    print("     |     \|/")
    print("     |      |")
    print("     |     / \\")
    print("     |    /   \\")
    print("     |")
    print("_____|_______")
    
def print_hand2():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    print("     |    _ | _")
    print("     |     \|/")
    print("     |      |")
    print("     |     / \\")
    print("     |    /   \\")
    print("     |")
    print("_____|_______")

def print_foot1():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    print("     |    _ | _")
    print("     |     \|/")
    print("     |      |")
    print("     |     / \\")
    print("     |   _/   \\")
    print("     |")
    print("_____|_______")
    
def print_foot2():
    print("      _______")
    print("     |      _|")
    print("     |     / \\")
    print("     |     \_/")
    print("     |    _ | _")
    print("     |     \|/")
    print("     |      |")
    print("     |     / \\")
    print("     |   _/   \_")
    print("     |")
    print("_____|_______")

# Runs these calls as long as dashes are still present in "dashes" and user
# has more than 0 guesses left
while dashes.find("-") != -1 and guesses_left > 0:
    if guesses_left == 10:
        print_hang_stand()
    elif guesses_left == 9:
        print_head()
    elif guesses_left == 8:
        print_torso()
    elif guesses_left == 7:
        print_arm1()
    elif guesses_left == 6:
        print_arm2()
    elif guesses_left == 5:
        print_leg1()
    elif guesses_left == 4:
        print_leg2()
    elif guesses_left == 3:
        print_hand1()
    elif guesses_left == 2:
        print_hand2()
    else:
        print_foot1()
    print(dashes)
    print(str(guesses_left) + " incorrect guesses left.")
    guess = get_guess()
    # Subtract 1 from guesses_left if guess was incorrect
    if guess not in secret_word:
        guesses_left = guesses_left - 1
    dashes = update_dashes(secret_word, dashes, guess)

# If user does not have dashes left in "dashes", congratulate them for winning
if dashes.find("-") == -1:
    print("Congrats! You win. The word was: " + secret_word)
# If user ran out of guesses, end game
else:
    print_foot2()
    print("You lose. The word was: " + secret_word)

sys.exit()

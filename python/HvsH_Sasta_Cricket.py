import random as rm
from time import sleep
import sys
import time

def get_masked_input(prompt=""):
    print(prompt, end='', flush=True)  # Print prompt without newline
    input_chars = []

    while True:
        char = sys.stdin.read(1)  # Read one character at a time
        if char in ('\n', '\r'):  # Break on Enter
            break
        elif char == '\x7f':  # Handle backspace
            if input_chars:
                input_chars.pop()
                # Move cursor back, overwrite with space, and move back again
                sys.stdout.write('\b \b') 
                sys.stdout.flush()
        else:
            input_chars.append(char)  # Store the input character
            print('*', end='', flush=True)  # Print '*' for each character typed

    print()  # Move to the next line after input is complete
    return ''.join(input_chars)

# Example usage
user_input = get_masked_input("Player 1 Hit: ")
print("Input captured:", user_input)  # This shows the actual input for demonstration purposes


# def get_single_digit_input():
#     while True:
#         print("Player 1 Hit: ", end="",flush=True)
#         # Check if the input is a single digit between 0 and 6
#         if input_value.isdigit() and len(input_value) == 1 and 0 <= int(input_value) <= 6:
#              # Display the masked output
#             return int(input_value)  # Return the input as an integer
#         else:
#             print("\nInvalid input! Please enter a digit between 0 and 6.")  # Prompt again

# # Usage

# user_input = get_single_digit_input("")
# print("*",end="",flush=True)
# print("\nYour input was:", user_input)  # Show the input value for confirmation


# def get_single_digit_input(prompt):
#     while True:
#         print(prompt, end="")  # Print prompt without a newline
#         input_value = getpass.getpass("")  # Get hidden input

#         # Check if the input is a single digit between 0 and 6
#         if input_value.isdigit() and len(input_value) == 1 and 0 <= int(input_value) <= 6:
#             print(" *")  # Display the masked output with asterisk on the same line
#             return int(input_value)  # Return the input as an integer
#         else:
#             print("\nInvalid input! Please enter a digit between 0 and 6.")  # Prompt again

# # Usage
# user_input = get_single_digit_input("Player 1 Hit: ")
# print("\nYour input was:", user_input)  # Show the input value for confirmation


# Defined a custom print function with flush
def fprint(*args, delay=0, **kwargs):
    print(*args, **kwargs, flush=True)  # Flush immediately
    if delay > 0:
        sleep(delay)

def print_word_by_word(text, delay=0.07):
    words = text.split()  # Split the text into words
    for word in words:
        print(word, end=' ')  # Print the word followed by a space
        sleep(delay)  # Wait for the specified delay
    print("\n")
    

def print_lbyl(text, delay=0.07):
    words = text.split()  # Split the text into words
    for word in words:
        for letter in word:
            print(letter, end='', flush=True)  # Print the word followed by a space
            sleep(delay)  # Wait for the specified delay
        print(end=" ", flush=True)
        
    return ""

def welcome():
    print_lbyl("Loading...")
    for i in range(3,0,-1):
        sleep(1)
        print(i, end="...")
        
    sleep(1)
    
    print_word_by_word("Welcome to the Sasta Cricket Game!")
    print()
    print_word_by_word("Simple Rules:")
    print_word_by_word("1. Choose numbers between 0 and 6.")
    print_word_by_word("2. Bowler tries to match their number with the batsman's.")
    print_word_by_word("3. If they match, the batsman is out.")
    print_word_by_word("4. If not, the batsman's number adds to their score.")
    print_word_by_word("5. Players swap roles after a match.")
    print_word_by_word("6. The new batsman tries to beat the previous score.")
    print()
    

    
def match():
    player1_score = 0
    player2_score = 0
    
    print("\nMatch Started!")
    # play1_hand = get_hidden_input("Player 1 Hit: ")
    print("\nMatch Started!")
    
    
# match()
def sastaCricket():
    
    # welcome()
    
    ch1 = input("\nEnter 'Y' to continue: ").strip().lower()
        
    if ch1 != "y":
        print("Exiting the game... Goodbye! :)")
        exit(0)
        

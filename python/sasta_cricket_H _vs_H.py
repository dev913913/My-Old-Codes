import random as rm
from time import sleep
import sys
import msvcrt  # For Windows key handling
import os  # Importing the os module for clearing the screen

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def masked_input(prompt=""):
    print(prompt, end='', flush=True)  # Print prompt without newline
    input_chars = []

    while True:
        char = msvcrt.getch()  # Read a single character (no echo)

        if char in (b'\r', b'\n'):  # Break on Enter
            if len(input_chars) == 1:  # Check if we have one character
                digit = input_chars[0]
                if digit.isdigit() and 0 <= int(digit) <= 6:  # Validate the input
                    print()  # Move to the next line
                    return int(digit)  # Return the integer value
                else:
                    print("\nInvalid input! Please enter a single digit between 0 and 6.")
                    print(prompt, end='', flush=True)  # Re-prompt
                    input_chars = []  # Clear input
            else:
                print("\nInvalid input! Please enter a single digit between 0 and 6.")
                print(prompt, end='', flush=True)  # Re-prompt
                input_chars = []  # Clear input
        elif char == b'\x08':  # Handle backspace (delete character)
            if input_chars:
                input_chars.pop()
                # Move cursor back, overwrite with space, and move back again
                sys.stdout.write('\b \b')
                sys.stdout.flush()
        elif char.isdigit() and len(input_chars) < 1:  # Allow only one digit
            input_chars.append(char.decode('utf-8'))  # Store the input character
            print('*', end='', flush=True)  # Print '*' for the character typed

# Example usage



# # Example usage
# user_input = get_masked_input("Player 1 Hit: ")
# print("Input captured:", user_input)  # Display the captured input for confirmation

def print_word_by_word(text, delay=0.07):
    words = text.split()  # Split the text into words
    for word in words:
        print(word, end=' ')  # Print the word followed by a space
        sleep(delay)  # Wait for the specified delay
    print("\n")
    

def print_lbyl(text, delay=0.05):
    words = text.split()  # Split the text into words
    for word in words:
        for letter in word:
            print(letter, end='', flush=True)  # Print the word followed by a space
            sleep(delay)  # Wait for the specified delay
        print(end=" ", flush=True)
    print("")
        
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
    
def compare_score(p1n="Player 1",p2n="Player 2",p1score=0, p2score=0):
    if p1score > p2score:
        print(f"\nHehe! {p1n} has won with extra {p1score-p2score} runs")
    elif p1score == p2score:
        print(f"\nIt's a draw at :{p1score} runs")  
    else: print(f"\nHehe! {p2n} has won with extra {p2score-p1score} runs") 
    
def match(p1n="Player 1",p2n="Player 2"):
    player1_score = 0
    player2_score = 0
    
    print("\nMatch 1 Started!")
    # i = 0
    while True:
        # if(i>0):
        #     print(f"\n{p1n}'s current score: '{player1_score}'\n")
        print("")
        play1_hand = masked_input(f"{p1n} Hit: ")
        play2_hand = masked_input(f"{p2n} Bowled: ")
        print("")
        print_lbyl(f"\n{p1n} hit: '{play1_hand}'")
        print_lbyl(f"{p2n} Bowled: '{play2_hand}'")
        

        if play1_hand == play2_hand:
            print("")
            print_lbyl(f"\n{p1n} is out at '{player1_score}'")
            break
        player1_score += play1_hand
        print("")
        print_lbyl(f"\n{p1n}'s current score: '{player1_score}'\n")
        input("Press Enter to continue...")
        clear_screen()


    print(f"\n{p2n}'s Target: '{player1_score +1 }' or more runs to win")
    input("Press Enter to continue...")
    clear_screen()

    
    print("\nMatch 2 Started!")  
        
    while True:
        print("")
        play2_hand = masked_input(f"{p2n} Hit: ")
        play1_hand = masked_input(f"{p1n} Bowled: ")
        print("")

        print_lbyl(f"\n{p2n} hit: '{play2_hand}'")
        print_lbyl(f"{p1n} bowled: '{play1_hand}'")

        if play1_hand == play2_hand:
            print_lbyl(f"\n{p2n} is out at '{player2_score}'")
            break
        player2_score += play2_hand
        print_lbyl(f"\n{p2n}'s current score: '{player2_score}'")
        if player2_score >= player1_score + 1:
            compare_score(p1n,p2n,player1_score, player2_score)
            break
        else:
            print(f"\n{p2n} needs at least '{player1_score-player2_score+1}' runs to win\n")
            input("Press Enter to continue...")
            clear_screen()

    
    return
    
    
def name_input():
    player1_name = input("\nEnter Player 1's Name: ")
    player2_name = input("Enter Player 2's Name: ")
    
    
    return player1_name, player2_name
    
# match()
def sastaCricket():
    
    welcome()
    
    
    ch1 = input("\nEnter 'Y' to continue: ").strip().lower()

      
    if ch1 != "y":
        print("Exiting the game... Goodbye! :)")
        exit(0)

    clear_screen()

    p1name, p2name = name_input()

    while True:
    
        clear_screen()

        match(p1name, p2name)

        ch3 =  input("\nDo you want to play again? (Y/N): ").strip().lower()
        if ch3!= "y":
            print("Exiting the game... Goodbye! :)")
            break
        clear_screen()

if __name__ == "__main__":
    sastaCricket()
        
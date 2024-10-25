import random as rm
from time import sleep

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
            print(letter, end='')  # Print the word followed by a space
            sleep(delay)  # Wait for the specified delay
        print(end=" ")
        
    return ""
        
def verify(n):
    return 0 <= n <= 6

def compare_score(comp_score, user_score):
    if comp_score > user_score:
        print(f"\nHehe! Computer has won with extra {comp_score-user_score} runs")
    elif comp_score == user_score:
        print("\nIt's a draw!") 
    else: print(f"\nCongratulations! You have won with extra {user_score-comp_score} runs") 
            
def comp_bat(comp_score, user_score, uf, cf):
    
    if uf == 1:
        print(f"Bowl out computer before it scores more than '{user_score}'")
        
    # print("\nComputer's turn")
    print("\n")
    print_lbyl("Bowl: ")
    while True:
        comp_hand = rm.randint(1,6)
        try:                                                   
            user_hand = int(input()) 
            
            while not verify(user_hand):
                sleep(0.7)
                print("\nInvalid Choice! Bowl only between '0' and '6'\n")
                user_hand = int(input(F"{print_lbyl("Bowl again: ")}"))
                
        
            if user_hand == comp_hand :
                sleep(0.6)
                print(f"Computer hit: {comp_hand}")
                sleep(1)
                print(f"Computer is out at {comp_score}")
                sleep(1)
                
                if uf == 1:
                    compare_score(comp_score, user_score)
                    break
                else: 
                    user_bat(comp_score, user_score, uf, cf)
                    break 
                    
            else:
                comp_score += comp_hand
                sleep(0.6)
                print(f"Computer hit: {comp_hand}")
                # print(f"But you bowled: {user_hand}")
                sleep(1)
                print(f"Comp's current score: {comp_score}")
        
        except ValueError:
            print("\nInvalid input! Please enter an integer.\n")
            print_lbyl("Bowl again: ")
            
        else: 
            sleep(1) 
            print("\n")
            print_lbyl("Bowl: ") 
    return comp_score
    
def user_bat(comp_score, user_score, uf, cf):
    
    if cf == 1:
        print(f"Your target is to score more than '{comp_score}'")
    
    print("\n")
    print_lbyl("Hit: ")
    while True:
        try:
            user_hand = int(input())  # Prompt for input once here

            # Validate user input
            while not verify(user_hand):
                sleep(0.7)
                print("\nInvalid Choice! Bowl only between '0' and '6'\n")
                user_hand = int(input(f"{print_lbyl("Hit again: ")}"))  # Re-prompt the user for input
            
            comp_hand = rm.randint(1, 6)

            if comp_hand == user_hand:
                sleep(0.6)
                print(f"Computer bowled: {comp_hand}")
                sleep(1)        
                print(f"You're out at {user_score}")
                sleep(1)
                
                if cf == 1:
                    compare_score(comp_score, user_score)
                    break
                else: 
                    comp_bat(comp_score, user_score, uf, cf)
                    break 
            
            
            else:
                user_score += user_hand
                sleep(0.6)
                print(f"Computer bowled: {comp_hand}")
                sleep(1)
                print(f"Your current score: {user_score}")

        except ValueError:
            print("\nInvalid input! Please enter an integer.\n")
            print_lbyl("Hit again: ")
            
        else:
            sleep(1) 
            print("\n")
            print_lbyl("Hit: ")    
    return user_score 
        
def sastaCricket():
    
    print()
    print_lbyl("Loading...")
    for i in range(3,0,-1):
        sleep(1)
        print(i, end="...")
        
    sleep(1)
    
    print_word_by_word("\nWelcome to the Sasta Cricket Game!")
    print()
    print_word_by_word("Simple Rules:")
    print_word_by_word("1. Choose numbers between 0 and 6.")
    print_word_by_word("2. Bowler tries to match their number with the batsman's.")
    print_word_by_word("3. If they match, the batsman is out.")
    print_word_by_word("4. If not, the batsman's number adds to their score.")
    print_word_by_word("5. Players swap roles after a match.")
    print_word_by_word("6. The new batsman tries to beat the previous score.")
    print()
    ch1 = input("\nEnter 'Y' to continue: ").strip().lower()
        
    if ch1 != "y":
        print("Exiting the game... Goodbye! :)")
        exit(0)
        
    while True:
        comp_score = 0
        user_score = 0
        
        print("\nWhat would you like to do first: \n")
        print(" [1] Batting")
        print(" [2] Bowling\n")
        

        while True:
            ch2 = input("Enter 1 or 2: ")
            match ch2:
                case '1':
                    user_bat(comp_score, user_score,1, 0)
                    break    
                case '2':
                    comp_bat(comp_score, user_score,0,1)
                    break 
                case _:
                    print("\nInvalid Choice!\n")
                    
        # if uf > 0:
        #     print(f"\nBowl out Computer before he scores more than {user_score}")
        #     comp_bat(comp_score, user_score)
               
        # else: 
        #     print(f"\nYour target is to score more than {comp_score}")
        #     user_score = user_bat(comp_score, user_score)
        #     if comp_score > user_score:
        #         print(f"\nHehe! Computer has won with extra {comp_score-user_score} runs")
        #     elif comp_score == user_score:
        #         print("It's a draw!") 
        #     else: print(f"\nCongratulations! You have won with extra {user_score-comp_score} runs")
            
        ch3 =  input("\nDo you want to play again? (Y/N): ").strip().lower()
        if ch3!= "y":
            print("Exiting the game... Goodbye! :)")
            break
        print("\n")
    
if __name__ == "__main__":
    sastaCricket()

    
        
       
import random as rm

def verify(n):
    if n >=1 and n<=6:
        return True
    else: return False
    
    
def user1_bat(user_1_score, user_2_score):
    user1_hand = rm.randint(1,6)
    while True:
        user_2_hand = int(input("\nBowl: "))
        while not verify(user_2_hand):
            user_2_hand = int(input("\nBat between only '0' and '6' "))
            continue
    
        if user_2_hand == user1_hand :
            print(f"'Player 1' hit: {user1_hand}")
            print(f"'Player 1' is out at {user_1_score}")
            break
        else:
            user_1_score += user1_hand
            print(f"'Player 1' hit: {user1_hand}")
            print(f"But you bowled: {user_2_hand}")
            print(f"'Player 1's current score: {user_1_score}")
    return user_1_score
    
def user2_bat(user_1_score, user_2_score):
    while True:
        user_2_hand = int(input("\nBat: "))
        while not verify(user_2_hand):
            user_2_hand = int(input("\nBat between only '0' and '6' "))
            continue
            
        user1_hand = rm.randint(1,6)
    
        if user1_hand == user_2_hand:
            print(f"'Player 1' bowled: {user1_hand}")
            print(f"'Player 2' out at {user_2_score}")
            break
        else:
            user_2_score += user_2_hand
            print(f"'Player 1' bowled: {user1_hand}")
            print(f"'Player 2' current score: {user_2_score}")
    return user_2_score        
        

while True: 
    print("Welcome to the Sasta Cricket Game!\n")
    print("Simple Rules:\n")
    print("  1. Choose numbers between 0 and 6.")
    print("  2. Bowler tries to match their number with the batsman's.")
    print("  3. If they match, the batsman is out.")
    print("  4. If not, the batsman's number adds to their score.")
    print("  5. Players swap roles after a match.")
    print("  6. The new batsman tries to beat the previous score.")

    ch1 = input("\nEnter 'Y' to continue: ")

    if ch1.lower() != "y":
       break
   
    user_1_score = 0
    user_2_score = 0
    
    print("\nWhat would 'player 1' like to choose: \n")
    print(" [1] Head")
    print(" [2] Tail\n")
    
    ch2 = int(input("Enter 1 or 2: "))
   
    arr = ["Head", "Tail"]
    
    h_or_t = rm.randint(1,2)
    
    if h_or_t == ch2:
        print(f"'Player 1' won the toss. It's {arr[h_or_t - 1]}\n")
        print("\nWhat would 'player 1' like to do first: \n")
    else: 
        print(f"'Player 2' won the toss. It's {arr[h_or_t - 1]}\n")
        print("\nWhat would 'player 2' like to do first: \n")
     
    print(" [1] Batting")
    print(" [2] Bowling\n")   
    
    
    ch2 = int(input("Enter 1 or 2: "))

    uf = 0
    match ch2:
        case 1:
            user_2_score = user2_bat(user_1_score, user_2_score)
            uf += 1    
        case 2:
            user_1_score = user1_bat(user_1_score, user_2_score) 
        case _:
            print("Invalid Choice!")
    if uf > 0:
        print(f"Bowl out 'player 1' before he scores more than {user_2_score}")
        user_1_score = user1_bat(user_1_score, user_2_score)
        if user_1_score > user_2_score:
            print(f"Hehe! 'player 1' has won with extra {user_1_score-user_2_score} runs")
        elif user_1_score == user_2_score:
            print("It's a draw!") 
        else: print(f"Congratulations! You have won with extra {user_2_score-user_1_score} runs")    
    else: 
        print(f"Your target is to score more than {user_1_score}")
        user_2_score = user2_bat(user_1_score, user_2_score)
        if user_1_score > user_2_score:
            print(f"Hehe! 'player 1' has won with extra {user_1_score-user_2_score} runs")
        elif user_1_score == user_2_score:
            print("It's a draw!") 
        else: print(f"Congratulations! You have won with extra {user_2_score-user_1_score} runs")  

    
        
       
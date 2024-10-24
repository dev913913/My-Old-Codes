import random as rm

# bool verifyn(n):
#     n == 1

def verify(n):
    if n >=1 and n<=6:
        return True
    else: return False
    
    
def comp_bat(comp_score, user_score):
    comp_hand = rm.randint(1,6)
    while True:
        user_hand = int(input("\nBowl: "))
        while not verify(user_hand):
            print("\nInvalid Choice! Bat between only '0' and '6' ")
            user_hand = int(input("Bowl again: "))
            print("")
            continue
    
        if user_hand == comp_hand :
            print(f"Computer hit: {comp_hand}")
            print(f"Computer is out at {comp_score}")
            break
        # elif comp_score > user_score:
        #     compiler_score += comp_hand
        else:
            comp_score += comp_hand
            print(f"Computer hit: {comp_hand}")
            # print(f"But you bowled: {user_hand}")
            print(f"Comp's current score: {comp_score}")
    return comp_score
    
def user_bat(comp_score, user_score):
    while True:
        user_hand = int(input("\nHit: "))
        while not verify(user_hand):
            print("\nInvalid Choice! Bat between only '0' and '6' ")
            user_hand = int(input("Bowl again: "))
            print("")
            continue
            
        comp_hand = rm.randint(1,6)
    
        if comp_hand == user_hand:
            print(f"Computer bowled: {comp_hand}")
            print(f"You're out at {user_score}")
            break
        else:
            user_score += user_hand
            print(f"computer bowled: {comp_hand}")
            # print(f"But you hit: {user_hand}")
            print(f"Your current score: {user_score}")
    return user_score        
        

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
   
    comp_score = 0
    user_score = 0
    
    print("\nWhat would you like to do first: \n")
    print(" [1] Batting")
    print(" [2] Bowling\n")
    ch2 = int(input("Enter 1 or 2: "))
    uf = 0
    match ch2:
        case 1:
            user_score = user_bat(comp_score, user_score)
            uf += 1    
        case 2:
            comp_score = comp_bat(comp_score, user_score) 
        case _:
            print("Invalid Choice!")
    if uf > 0:
        print(f"Bowl out Computer before he scores more than {user_score}")
        comp_score = comp_bat(comp_score, user_score)
        if comp_score > user_score:
            print(f"Hehe! Computer has won with extra {comp_score-user_score} runs")
        elif comp_score == user_score:
            print("It's a draw!") 
        else: print(f"Congratulations! You have won with extra {user_score-comp_score} runs")    
    else: 
        print(f"Your target is to score more than {comp_score}")
        user_score = user_bat(comp_score, user_score)
        if comp_score > user_score:
            print(f"Hehe! Computer has won with extra {comp_score-user_score} runs")
        elif comp_score == user_score:
            print("It's a draw!") 
        else: print(f"Congratulations! You have won with extra {user_score-comp_score} runs")
        
    ch3 =  input("\nDo you want to play again? (Y/N): ").strip().lower()
    if ch3!= "y":
        print("")
        break
        

    
        
       
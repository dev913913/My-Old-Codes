#trying out algorithms that i wrote last day, sunday, on star patterns by figuring out things by myself. some credit goes to Vikas Sir

# pattern 1: Left Diagonal
def left_diagonal(n,p):
    print("\nLeft Diagonal: ")
    for i in range(1,n+1):
        for j in range(i):
            print(p, end="")
        print()

# pattern 2: Right Diagonal
def right_diagonal(n,p):
    print("\nRight Diagonal: \n")
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(i):    
            print(p, end="")
        print("")

# pattern 3: Pyramid
def Pyramid(n,p):
    print("\nPyramid: \n")
    for i in range(0,n):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(0,1+(2*i)):    
            print(p, end="")
        print("")


# pattern 4: Inverse Pyramid
def inverse_pyramid(n,p):
    print("\nInverse Pyramid: \n")
    for i in range(0,n):
        for j in range(0,i):
            print(" ", end="")
        for k in range(0-2,n-(2*i)):    
            print(p, end="")
        print("")


# pattern 5: Diamond
def Diamond(n,p):
    print("\nDiamond: \n")
    for i in range(0,n+1):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(0,1+(2*i)):    
            print(p, end="")
        print("")
    for i in range(0,n):
        for j in range(0,i):
            print(" ", end="")
        for k in range(((n+(2*i)),0,-1)):    
            print(p, end="")
        print("")


# Main function

# if "__name__" == "__main__":
while True:
    print("\nChoose the pattern you want to create: \n")
    print(" [1] Left Diagonal")
    print(" [2] Right Diagonal")
    print(" [3] Pyramid")
    print(" [4] Inverse Pyramid")
    print(" [5] Diamond")
    print(" [0] Quit")

    choice = int(input("\nEnter your choice (0-5): "))
    
    if choice == 0:
        print("\nExiting the program.")
        break
    elif choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice== 5:
        pass
    else:
        print("\nInvalid choice. Please enter a number between 0 and 5.")
        continue

    n = int(input("\nEnter the number of rows for the pattern (0 to quit): "))
    if n == 0:
        break
    elif n < 0:
        print("\nInvalid input. Please enter a positive number.")
        continue
    
    p = input("\n Enter the pattern symbol: ")
    if n == 1:
        print("\nSingle row star pattern: \n")
        print(p)
        continue
   

    
    

    match choice:
        case 1:
            left_diagonal(n, p)
        case 2:
            right_diagonal(n, p)
            
        case 3:
            Pyramid(n, p)
            
        case 4:
            inverse_pyramid(n, p)
            
        case 5:
            n = int(n//2)
            print(n)
            Diamond(n, p)
            
        case _:
            print("\nInvalid choice. Please enter a number between 0 and 5.")
            continue
    
    ch = input("Do you want to try again?Y/N: ")
    if ch.lower() == "y":
        continue
    else: break

    

        

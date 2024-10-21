#trying out algorithms that i wrote last day, sunday, on star patterns by figuring out things by myself. some credit goes to Vikas Sir


# Square

def square(n,p):
    print("\n[1] Square: \n")
    for i in range(0,n):
        print("    ", end="")
        for j in range(0,n):
            print(p, end=" ")
        print()
        
def rectangle(l,w,p):
    print("\n[2] Rectangle: \n")
    for i in range (0,l):
        print("    ", end="")
        for j in range (0,w):
            print(p, end=" ")
        print("")
        
# pattern 1: Left Diagonal
def left_diagonal(n,p):
    print("\n[3] Left Diagonal: \n")
    for i in range(1,n+1):
        print("    ", end="")
        for j in range(i):
            print(p, end=" ")
        print("")

# pattern 2: Right Diagonal
def right_diagonal(n,p):
    print("\n[4] Right Diagonal: \n")
    for i in range(1,n+1):
        print("", end="   ")
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(i):    
            print(p, end=" ")
        print("")

# pattern 3: Pyramid
def Pyramid(n,p):
    print("\n[5] Pyramid: \n")
    for i in range(0,n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for k in range(0,1+(2*i)):    
            print(p, end=" ")
        print("")


# pattern 4: Inverse Pyramid
def inverse_pyramid(n,p):
    max_p = (1 + n*2)-2
    print("\n[6] Inverse Pyramid: \n")
    for i in range(0,n):
        for j in range(i):
            print(" ", end=" ")
        for k in range(max_p-(2*i)):        
            print(p, end=" ")
        print("")


# pattern 5: Diamond
def Diamond(n,p):
    print("\n[7] Diamond: \n")
    for i in range(0,n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for k in range(0,1+(2*i)):    
            print(p, end=" ")
        print("")
    max_p = (1 + n*2)-2
    for i in range(1,n):
        for j in range(i):
            print(" ", end=" ")
        for k in range(max_p-(2*i)):    
            print(p, end=" ")
        print("")


# Main function

# if "__name__" == "__main__":
while True:
    print("\nChoose the pattern you want to create: \n")
    print(" [1] Square")
    print(" [2] Rectangle")
    print(" [3] Left Diagonal")
    print(" [4] Right Diagonal")
    print(" [5] Pyramid")
    print(" [6] Inverse Pyramid")
    print(" [7] Diamond")
    print(" [0] Quit")

    choice = int(input("\nEnter your choice (0-5): "))
    
    if choice == 0:
        print("\nExiting the program.")
        break
    elif choice == 2:
        l = int(input("\n Enter the length of the rectangle: "))
        w = int(input("\n Enter the width of the rectangle: "))
        
    elif (choice == 1) or (choice >=3 and choice <= 7):
        n = int(input(f"\nEnter the size (or 0 to quit): "))
        if n == 0:
            print("\nExiting the program.")
            break
        elif n == 1:
            print("\nSingle row star pattern: \n")
            print(p)
            continue

        elif n < 0:
            print("\nInvalid input. Please enter a positive number.")
            continue 

    elif choice > 7:
            print("\nInvalid choice. Please enter a number between 0 and 5.")
            continue
       
    p = input("\nEnter the pattern symbol: ") 
   
    
    
   

    
    

    match choice:
        case 1:
            square(n, p)
        case 2:
            rectangle(l,w, p)
            
        case 3:
            left_diagonal(n, p)
        case 4:
            right_diagonal(n, p)
            
        case 5:
            Pyramid(n, p)
            
        case 6:
            inverse_pyramid(n, p)
            
        case 7:
            # n = int(n//2)
            # print(n)
            Diamond(n, p)
            
        case _:
            print("\nInvalid choice. Please enter a number between 0 and 5.")
            continue
    
    ch = input("\nDo you want to try again?Y/N: ")
    if ch.lower() == "y":
        continue
    else: break

    

        

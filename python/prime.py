a = int(input("Enter your number\n"))

if a==0 or a==1:
        print(f"{a} is a not a prime no.")
else:
    for i in range(2,a):
        if a%i==0:
            print(f"{a} is not a prime no.")
            break
    else: print(f"{a} is a prime no.")
    

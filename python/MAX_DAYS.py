from date_finder import leapyear

year = int(input("Enter the year whose max days you wanna find: "))

if leapyear(year):
    print(f"The {year} has maximum '366' days as it a leap year")
else:
    print(f"The {year} has maximum '365' days as it not a leap year")

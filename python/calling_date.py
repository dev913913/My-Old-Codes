from date_finder import date_modifier

# import calendar

# help(calendar)

# cal = calendar

# cal.setfirstweekday
df = date_modifier

def enter_date_on_ter():
    print("Down below, enter the manufacturing date")
    day = int(input("Enter the day number: "))
    while True:
        if day<=31:
            break
        else:
            print(f"Invalid date! {day} is more than 31 days.")
            day = int(input("Enter the day number again: "))

    month = int(input("Enter the month number: "))
    while True:
        if month<=12:
            break
        else:
            print(f"Invalid date! {month} is more than 12 months ")
            month = int(input("Enter the month number again: "))
    while True:
            if valid_date(day, month, year):
                break
            else:
                print(f"Invalid date! {day} is more than \n the maximum {days_in_month( month, year)} days  in the given month {month} of year {year}.")
                day = int(input("Enter the day number again: ")) 
    year = int(input("Enter the year numer: "))
    df(day,month,year)
            
enter_date_on_ter()




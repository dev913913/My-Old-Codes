def leapyear(year):
    # one way to check if year is leap year or not
    if (year%4)==0:
        if (year%100)!=0:
            return True
        else:
            if (year%400)==0:
                return True
            else: return False
    else: 
        return False
    
    # another way to check so
    
    
    # if (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0):
    #     return True
    # else:
    #     return False
    
def days_in_month( month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leapyear(year):
            return 29
        else:
            return 28
    else:
        return 31

def valid_date(day, month, year):
    if day < days_in_month(year, month):
        return True
    else: return False
    

def date_modifier(day, month, year):
    while True:
        # print("Down below, enter the manufacturing date")
        # day = int(input("Enter the day number: "))
        while True:
            if day<=31:
                break
            else:
                print(f"Invalid date! \nMaximum no. of days a month can ever have are 31 days\n {day} is more than 31 days.")
                day = int(input("Enter the day number again: "))

        # month = int(input("Enter the month number: "))
        while True:
            if month<=12:
                break
            else:
                print(f"Invalid date! {month} is more than 12 months ")
                month = int(input("Enter the month number again: "))
        # year = int(input("Enter the year numer: "))
        # print(f"Old date: {day}-{month}-{year}")
        
        # getting the month given's max days and also checking  if the the date givn is under that
        
        while True:
            if valid_date(day, month, year):
                break
            else:
                print(f"Invalid date! {day} is more than \n the maximum {days_in_month( month, year)} days  in the given month {month} of year {year}.")
                day = int(input("Enter the day number again: ")) 


         
        maxdays = days_in_month( month, year)
        if day <10 and month >= 10:
            print(f"Old date: 0{day}-{month}-{year} ")
        elif day >=10 and month < 10:
            print(f"Old date: {day}-0{month}-{year} ")  
        elif day<10 and month <10:
            print(f"Old date: 0{day}-0{month}-{year} ")                     
        else:
            print(f"Old date date: {day}-{month}-{year}")
        incr = int(input("Days to be added: "))
        new_day = day + incr
        # new_month = 0
        if new_day<=maxdays:
            # flr_div = new_day//31
            # print(f"floor divion gave {flr_div}")
            pass
        else:
            new_month = new_day//maxdays
            # print(f"floor divion gave {new_month}")
            month = month + new_month
            new_day = new_day%maxdays
            

        if month<=12:
            # flr_div = new_day//31
            # print(f"floor divion gave {flr_div}")
            pass
        else:
            # month = month + new_month
            # print(f"floor divion gave {flr_div}")
            flr_div = month//12
            # print(f"floor divion gave {flr_div}")
            year += (flr_div)
            month = (month%12)
        if new_day <10 and month >= 10:
            print(f"New date: 0{new_day}-{month}-{year} ")
        elif new_day >=10 and month < 10:
            print(f"New date: {new_day}-0{month}-{year} ")
        elif new_day<10 and month <10:
            print(f"New date: 0{new_day}-0{month}-{year} ")
        else:
            print(f"New date: {new_day}-{month}-{year}")
        
        print("\n____________________________\n")
        choice = input("Want to try again? Press Y/N: ")
        if choice.lower()=='y':
            print("____________________________\n")
            continue    
        else: break
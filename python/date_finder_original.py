# def old_date_reciever():
#     a = input("Enter your date in DD-MM-YYYY\n")
#     b = str(a).strip()
#     day = int(b[0:2])
#     month = int(b[3:5])
#     year = int(b[6:len(b)+1])
#     if day>30:
#         print(f"Invalid date! {day} is more than 30 days ")
#         exit()
#     if month>12:
#         print(f"Invalid date! {month} is more than 12 months ")
#         exit()

def leapyear(year):
    # one way to check if year is leap year or not
    if year%4==0:
        if year%100!=0:
            return True
        else:
            if year%400==0:
                return True
            else: return False
    else: 
        return False
    
    # another way to check so
    
    
    # if (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0):
    #     return True
    # else:
    #     return False
    
def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leapyear(year):
            return 29
        else:
            return 28
    else:
        return 31
    
def date_modifier(day, month, year):
    while True:
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
        year = int(input("Enter the year numer: "))
        
        # getting the month given's max days and also checking  if the the date givn is under that
        
        # if new_day > days_in_month(year, month):
        #     print(f"Invalid date! {day}-{month}-{year} is more than the maximum days in the given month.")
        #     continue
         
        # print(f"Old date: {day}-{month}-{year}")
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
        if new_day<=31:
            # flr_div = new_day//31
            # print(f"floor divion gave {flr_div}")
            pass
        else:
            new_month = new_day//31
            # print(f"floor divion gave {new_month}")
            month = month + new_month
            new_day = new_day%31
            

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
        if day <10 and month >= 10:
            print(f"New date: 0{new_day}-{month}-{year} ")
        elif day >=10 and month < 10:
            print(f"New date: {new_day}-0{month}-{year} ")
        elif day<10 and month <10:
            print(f"New date: 0{new_day}-0{month}-{year} ")
        else:
            print(f"New date: {new_day}-{month}-{year}")
        
        print("\n____________________________\n")
        choice = input("Want to try again? Press Y/N: ")
        if choice.lower()=='y':
            print("____________________________\n")
            continue    
        else: break

date_modifier(31,2,2024)

# def add():
#     print("add")
   
# if __name__ != '__main__':
#     add()
     
# if __name__ == '__main__':
#     date_modifier()




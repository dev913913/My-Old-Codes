import tkinter as tk
from tkinter import ttk

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month_ywise(month, year):
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31,
                     31, 30, 31, 30, 31]
    return days_in_month[month - 1]

def date_adder(day, month, year, days_to_add):
    while days_to_add > 0:
        days_in_current_month = days_in_month_ywise(month, year)
        if day + days_to_add <= days_in_current_month:
            day += days_to_add
            days_to_add = 0
        else:
            days_to_add -= (days_in_current_month - day + 1)
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
    return day, month, year

def add_days():
    # Get the selected date, month, and year from the dropdowns
    day = selected_date.get()
    month = selected_month.get()
    year = selected_year.get()
    # Get the number of days to add from the entry widget
    days_to_add = int(days_entry.get())
    
    # Calculate the new date using the date_adder function
    new_day, new_month, new_year = date_adder(day, month, year, days_to_add)
    
    # Display the new date
    result_label.config(text=f"New Date: {new_day:02d}-{new_month:02d}-{new_year}")

# Set up Tkinter window
root = tk.Tk()
root.title("Date Adder")
root.geometry("300x250")

# Variables for date, month, year
selected_date = tk.IntVar(value=1)
selected_month = tk.IntVar(value=1)
selected_year = tk.IntVar(value=2024)

# Create dropdowns
date_dropdown = ttk.OptionMenu(root, selected_date, *range(0, 32))
month_dropdown = ttk.OptionMenu(root, selected_month, *range(0, 13))
year_dropdown = ttk.OptionMenu(root, selected_year, *range(2000, 2101))

date_dropdown.pack(pady=1)
month_dropdown.pack(pady=5)
year_dropdown.pack(pady=9)

# Entry for days to add
days_entry = ttk.Entry(root)
days_entry.pack(pady=5)
days_entry.insert(0, "Enter days to add")

# Button to calculate new date
add_button = ttk.Button(root, text="Add Days", command=add_days)
add_button.pack(pady=5)

# Label to show the result
result_label = ttk.Label(root, text="")
result_label.pack(pady=5)

# Start Tkinter event loop
root.mainloop()

import tkinter as tk
import date_finder as df

def tk_display():
  root = tk.Tk() # iniitalise the main window
  root.title("Date Adder")

  # Setting the size of the window
  root.geometry("500x400") #width x height


  frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)  # Background color, padding
  frame.pack(padx=20, pady=20)

 # Label widget to display a message
  label = tk.Label(frame, text ="Enter the Old Date Below", font = "Arial,20")  
  label.pack()
  # This keepts the window open and waits for user interaction
  
  entry = tk.Entry(root)
  entry.pack()
  


  # Variables to hold the selected date, month, and year
selected_date = tk.StringVar()
selected_month = tk.IntVar()
selected_year = tk.StringVar()

# Set default values
selected_date.set(1)
selected_month.set(1)
selected_year.set(2024)

# Create dropdowns for date, month, and year
date_dropdown = tk.OptionMenu(root, selected_date, *range(1, 32))
month_dropdown = tk.OptionMenu(root, selected_month, *range(1, 13))
year_dropdown = tk.OptionMenu(root, selected_year, *range(1900, 2101))

# Position the dropdowns in the window
date_dropdown.pack(pady=5)
month_dropdown.pack(pady=5)
year_dropdown.pack(pady=5)
  


# Input for the number of days to add
days_entry = ttk.Entry(root)
days_entry.pack(pady=5)
days_entry.insert(0, "Enter days to add")  # Default text

def add_days():
    date = selected_date.get()
    month = selected_month.get()
    year = selected_year.get()
    days_to_add = int(days_entry.get())
    
    df.
    new_date, new_month, new_year = date_adder(date, month, year, days_to_add)
    
    # Display the new date
    result_label.config(text=f"New Date: {new_date:02d}-{new_month:02d}-{new_year}")

# Button to trigger the date calculation
add_button = ttk.Button(root, text="Add Days", command=add_days)
add_button.pack(pady=5)



root.mainloop()
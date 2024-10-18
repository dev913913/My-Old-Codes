import tkinter as tk


def tk_display():
  mainw = tk.Tk() # iniitalise the main window
  mainw.title("My First Ever Tkinter Window :")

  # Setting the size of the window
  mainw.geometry("500x400") #width x height


  frame = tk.Frame(mainw, bg="lightblue", padx=10, pady=10)  # Background color, padding
  frame.pack(padx=20, pady=20)

 # Label widget to display a message
  label = tk.Label(frame, text="Enter your name", font = "Arial,16")  
  label.pack()
  # This keepts the window open and waits for user interaction
  
  entry = tk.Entry(mainw)
  entry.pack()
  
  # Function to take input and print when the button is clicked
#   def hello():
#       name = entry.get()
#       print(f"Hello, {name}")
#     # name = entry.get()
#     # lable2 = tk.Label(mainw, text = name, font="Arial,16")
#     # label2.pack()

  # Variable to store the selected option
  selected_option = tk.StringVar()
  selected_option.set("Choose an option")  # Default option
  
  # Create the dropdown menu
  dropdown = tk.OptionMenu(mainw, selected_option, "Option 1", "Option 2", "Option 3")
  dropdown.pack()

    # Function to display the selected option
  def show_selection():
    name = entry.get()
    option = selected_option.get()
    print(f"Your Name: {name}, Select: {option}")   
      
  # Button widget to call the hello function
  button = tk.Button(mainw, text = "Submit", command=show_selection)
  button.pack()
  
  mainw.mainloop()


tk_display()
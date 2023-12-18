import tkinter as tk

# Function to update the display when buttons are clicked
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

# Function to clear the display
def clear_display():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the input and output
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Loop to create buttons and assign functionalities
for i, row in enumerate(buttons):
    for j, symbol in enumerate(row):
        if symbol == 'C':
            button = tk.Button(root, text=symbol, padx=40, pady=20, command=clear_display)
        elif symbol == '=':
            button = tk.Button(root, text=symbol, padx=40, pady=20, command=calculate)
        else:
            button = tk.Button(root, text=symbol, padx=40, pady=20, command=lambda value=symbol: button_click(value))
        button.grid(row=i + 1, column=j, padx=5, pady=5)

# Run the application
root.mainloop()

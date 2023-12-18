import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4 characters")
        return

    strength = strength_var.get()

    if strength == "Weak":
        characters = string.ascii_lowercase
    elif strength == "Medium":
        characters = string.ascii_letters + string.digits
    else:  # Strong
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Create the GUI
root = tk.Tk()
root.title("Password Generator")
root.configure()  

label_length = tk.Label(root, text="Enter Password Length:")  
label_length.pack()

length_entry = tk.Entry(root)
length_entry.pack()

label_strength = tk.Label(root, text="Select Password Strength:")  
label_strength.pack()

strength_var = tk.StringVar()
strength_var.set("Weak")

weak_radio = tk.Radiobutton(root, text="Weak", variable=strength_var, value="Weak" )  
weak_radio.pack()

medium_radio = tk.Radiobutton(root, text="Medium", variable=strength_var, value="Medium")  
medium_radio.pack()

strong_radio = tk.Radiobutton(root, text="Strong", variable=strength_var, value="Strong")  
strong_radio.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, )  
generate_button.pack()

password_entry = tk.Entry(root, show="")
password_entry.pack()

root.mainloop()

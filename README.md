#codsoft




PASSWORD:

Certainly! The provided Python code is a simple password generator GUI built using the tkinter library. Let's break down the code into sections:

Imports:

python
Copy code
import tkinter as tk
from tkinter import messagebox
import random
import string
Import necessary modules:
tkinter: GUI library.
messagebox: For displaying error messages.
random: For generating random values.
string: For working with string constants and functions.
Password Generation Function:

python
Copy code
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
This function is triggered when the "Generate Password" button is pressed.
It retrieves the desired password length and strength.
Based on the strength selected, it defines a set of characters (characters) to use for the password.
It generates a random password of the specified length using the chosen character set.
The generated password is then displayed in the GUI entry widget (password_entry).
GUI Initialization:

python
Copy code
root = tk.Tk()
root.title("Password Generator")
Create the main window with the title "Password Generator."
Labels and Entry Widgets for Password Length and Strength:

python
Copy code
label_length = tk.Label(root, text="Enter Password Length:")
label_length.pack()

length_entry = tk.Entry(root)
length_entry.pack()

label_strength = tk.Label(root, text="Select Password Strength:")
label_strength.pack()
Labels and entry widgets for inputting the password length and selecting the password strength.
Radio Buttons for Password Strength:

python
Copy code
strength_var = tk.StringVar()
strength_var.set("Weak")

weak_radio = tk.Radiobutton(root, text="Weak", variable=strength_var, value="Weak" )  
weak_radio.pack()

medium_radio = tk.Radiobutton(root, text="Medium", variable=strength_var, value="Medium")  
medium_radio.pack()

strong_radio = tk.Radiobutton(root, text="Strong", variable=strength_var, value="Strong")  
strong_radio.pack()
Radio buttons for selecting the password strength: "Weak," "Medium," or "Strong."
Generate Password Button:

python
Copy code
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()
Button that, when clicked, triggers the generate_password function.
Entry Widget for Displaying the Generated Password:

python
Copy code
password_entry = tk.Entry(root, show="")
password_entry.pack()
Entry widget for displaying the generated password. The show="" argument ensures that the characters are not visible.
Run the GUI:

python
Copy code
root.mainloop()
Start the main event loop to run the GUI. This loop waits for user interactions and updates the GUI accordingly.















CONTACT BOOK :


import tkinter as tk

def add_contact():
    name = name_var.get()
    number = number_var.get()
    if name and number:
        contact_list.insert(tk.END, f"{name}: {number}")
        name_var.set("")
        number_var.set("")

def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        contact_list.delete(selected_contact)

def edit_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Contact")
        edit_window.geometry("250x120")
        edit_window.configure(bg="lightgrey")

        name, number = contact_list.get(selected_contact).split(": ")
        edit_name_var = tk.StringVar(value=name)
        edit_number_var = tk.StringVar(value=number)

        edit_name_label = tk.Label(edit_window, text="Name:", bg="lightgrey")
        edit_name_label.pack()

        edit_name_entry = tk.Entry(edit_window, textvariable=edit_name_var)
        edit_name_entry.pack()

        edit_number_label = tk.Label(edit_window, text="Number:", bg="lightgrey")
        edit_number_label.pack()

        edit_number_entry = tk.Entry(edit_window, textvariable=edit_number_var)
        edit_number_entry.pack()

        def save_edit():
            contact_list.delete(selected_contact)
            contact_list.insert(selected_contact, f"{edit_name_var.get()}: {edit_number_var.get()}")
            edit_window.destroy()

        save_button = tk.Button(edit_window, text="Save", command=save_edit, bg="green", fg="white")
        save_button.pack()

root = tk.Tk()
root.title("Contact Book")
root.geometry("300x300")
root.configure(bg="lightgrey")

name_var = tk.StringVar()
number_var = tk.StringVar()

name_label = tk.Label(root, text="Name:", bg="lightgrey")
name_label.pack()

name_entry = tk.Entry(root, textvariable=name_var)
name_entry.pack()

number_label = tk.Label(root, text="Number:", bg="lightgrey")
number_label.pack()

number_entry = tk.Entry(root, textvariable=number_var)
number_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact, bg="blue", fg="white")
add_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg="red", fg="white")
delete_button.pack()

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact, bg="orange", fg="white")
edit_button.pack()

contact_list = tk.Listbox(root)
contact_list.pack()

root.mainloop()



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

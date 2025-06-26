import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
phonebook = {}

# Function to add contact
def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    age = age_var.get().strip()
    gender = gender_var.get().strip()
    profession = profession_var.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone Number are required.")
        return

    phonebook[name] = {
        "Phone": phone,
        "Age": age,
        "Gender": gender,
        "Profession": profession
    }

    messagebox.showinfo("Success", f"Contact for {name} added.")
    clear_fields()
    update_display()

# Function to search contact
def search_contact():
    name = name_var.get().strip()
    if name in phonebook:
        contact = phonebook[name]
        result = f"Name: {name}\nPhone: {contact['Phone']}\nAge: {contact['Age']}\nGender: {contact['Gender']}\nProfession: {contact['Profession']}"
        messagebox.showinfo("Contact Found", result)
    else:
        messagebox.showerror("Not Found", f"No contact found with name '{name}'.")

# Function to clear fields
def clear_fields():
    name_var.set("")
    phone_var.set("")
    age_var.set("")
    gender_var.set("")
    profession_var.set("")

# Function to update contact list display
def update_display():
    listbox.delete(0, tk.END)
    for name in phonebook:
        listbox.insert(tk.END, f"{name} - {phonebook[name]['Phone']}")

# GUI setup
root = tk.Tk()
root.title("Phonebook GUI")
root.geometry("400x500")

# Input Variables
name_var = tk.StringVar()
phone_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
profession_var = tk.StringVar()

# Labels and Entries
tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Phone Number").pack()
tk.Entry(root, textvariable=phone_var).pack()

tk.Label(root, text="Age").pack()
tk.Entry(root, textvariable=age_var).pack()

tk.Label(root, text="Gender").pack()
tk.Entry(root, textvariable=gender_var).pack()

tk.Label(root, text="Profession").pack()
tk.Entry(root, textvariable=profession_var).pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Clear Fields", command=clear_fields).pack(pady=5)

# Listbox to show contacts
tk.Label(root, text="Saved Contacts:").pack()
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Start the GUI loop
root.mainloop()

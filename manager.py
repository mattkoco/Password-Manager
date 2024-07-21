import random
import string
import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# function to generate a strong password
def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # define possible characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # ensure that the passwrod has at least one letter, one number, and one special character (@, #, $, etc.)
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # add some random characters to reach the desired lenght of the password
    password += random.choices(all_characters, k=length-3)
    
    # shuffle the characters so that its random
    random.shuffle(password)
    
    return ''.join(password)

# function to store a password
def store_password(service, username, password):
    filename = "passwords.json"
    
    # check if the file exists, and if not then create an empty dictionary
    if os.path.exists(filename):
        with open(filename, "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}
    
    # add the new password
    passwords[service] = {"username": username, "password": password}
    
    # save the passwords to the file
    with open(filename, "w") as file:
        json.dump(passwords, file, indent=4)

# function to retreive a password
def retrieve_password(service):
    filename = "passwords.json"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            passwords = json.load(file)
        
        if service in passwords:
            return passwords[service]
        else:
            return "Service not found."
    else:
        return "No passwords stored yet."

# functions for the GUI buttons
def generate_password_gui():
    length = simpledialog.askinteger("Password Length", "Enter the desired length of the password:")
    if length:
        try:
            password = generate_password(length)
            messagebox.showinfo("Generated Password", f"Password: {password}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def store_password_gui():
    service = simpledialog.askstring("Service", "Enter the name of the service:")
    username = simpledialog.askstring("Username", "Enter the username:")
    password = simpledialog.askstring("Password", "Enter the password:")
    if service and username and password:
        store_password(service, username, password)
        messagebox.showinfo("Success", f"Password for {service} stored successfully.")

def retrieve_password_gui():
    service = simpledialog.askstring("Service", "Enter the name of the service:")
    if service:
        credentials = retrieve_password(service)
        if isinstance(credentials, dict):
            messagebox.showinfo("Stored Password", f"Username: {credentials['username']}\nPassword: {credentials['password']}")
        else:
            messagebox.showinfo("Error", credentials)

# main function for the GUi
def main_gui():
    root = tk.Tk()
    root.title("Password Manager")
    
    tk.Button(root, text="Generate Password", command=generate_password_gui).pack(pady=10)
    tk.Button(root, text="Store Password", command=store_password_gui).pack(pady=10)
    tk.Button(root, text="Retrieve Password", command=retrieve_password_gui).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()

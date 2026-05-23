import random
import string
import tkinter as tk
from tkinter import messagebox

#generate password function
def generate_password():
    try:
        length = int(length_entry.get())
        
        if length <=0:
            messagebox.showerror("ERROR!","Enter a valid Password length")
            return
        
        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        all_characters = letters + numbers + symbols

        password = ""

        for i in range(length):
            password += random.choice(all_characters)
        
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    
    except ValueError:
        messagebox.showerror("ERROR!","Please Enter a Number")

#Save Password function
def save_password():
    password = password_entry.get()

    if password == "":
        messagebox.showerror("Warning","Generate a Password first")
        return
    
    with open("password.txt","a") as file:
        file.write("Current Password:"+password + "\n")
    
    messagebox.showinfo("Saved","Password Saved Successfully")

#GUI
root = tk.Tk()
root.title("PASSWORD GENERATOR")
root.geometry("500x300")
root.resizable(False,False)


title_label = tk.Label(
    root,
    text = "PASSWORD GENERATOR",
    font = ("Arial",20,"bold")
)
title_label.pack(pady = 10)

#length input
length_label = tk.Label(
    root,
    text = "Enter Password Length:"
)
length_label.pack()

length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)

# GenerateButton
generate_button = tk.Button(
    root,
    text = "Generate Password",
    command = generate_password,
    bg = "white",
    fg = "black",
    padx = 10,
    pady = 5
)
generate_button.pack(pady=10)


#display
password_entry = tk.Entry(
    root, 
    width = 35,
    font = ("Arial", 12)
)
password_entry.pack(pady = 5)

#Save button
save_button = tk.Button(
    root,
    text = "Save Password",
    command = save_password,
    bg = "white",
    fg = "black",
    padx = 10,
    pady = 5
)
save_button.pack(pady=5)

root.mainloop()


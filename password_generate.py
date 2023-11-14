'''
    Task 3
    Password generator
'''

import tkinter as tk
from tkinter import ttk
import secrets
import string

def Password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pd = ''.join(secrets.choice(characters) for _ in range(length))
    return pd

def button1():
    length = int(side_entry.get())
    pd = Password(length)
    ans_label.config(text=f"Generated Password: {pd}")


root= tk.Tk()
root.title("Password Generate")
root.geometry('500x300')
root.resizable(0,0)
root.configure(background='#CBC3E3')


side_label = ttk.Label(root, text="Password Length:")
side_entry = ttk.Entry(root)
button_1 = ttk.Button(root, text="Generate Password", command=button1)
ans_label = ttk.Label(root, text="Generated Password: ")


side_label.grid(row=1, column=0, padx=10, pady=10)
side_entry.grid(row=1, column=1, padx=10, pady=10)
button_1.grid(row=2, column=0, columnspan=2, pady=10)
ans_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

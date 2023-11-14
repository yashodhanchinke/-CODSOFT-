'''
     Task 5
     Contact Book
'''
import tkinter as tk
from tkinter import ttk

class Contact_Book:
    def __init__(self, root):
        self.root = root
        self.root.title("Store and Search by Contact")
        self.cont = {}

        
        ttk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky="w")

        
        self.enter_name = ttk.Entry(root)
        self.enter_phone_number = ttk.Entry(root)
        self.enter_emailId = ttk.Entry(root)
        self.address_entry = ttk.Entry(root)

        self.enter_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.enter_phone_number.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.enter_emailId.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Buttons
        ttk.Button(root, text="Add Contact", command=self.contact_Add).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(root, text="View Contact List", command=self.view_all_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(root, text="Search Contact", command=self.contact_search).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(root, text="Update Contact", command=self.contact_update).grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(root, text="Delete Contact", command=self.contact_delete).grid(row=8, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=9, column=0, columnspan=2, pady=10)

    def contact_Add(self):
        name = self.enter_name.get()
        phone = self.enter_phone_number.get()
        email = self.enter_emailId.get()
        address = self.address_entry.get()

        if name not in self.cont:
            self.cont[name] = {'Phone': phone, 'Email': email, 'Address': address}
            self.result_label.config(text=f"Contact '{name}' added successfully.")
        else:
            self.result_label.config(text=f"Contact '{name}' already exists.")

    def view_all_contacts(self):
        contact_list = "\n".join([f"{name}: {details['Phone']}" for name, details in self.cont.items()])
        self.result_label.config(text=f"Contact List:\n{contact_list}")

    def contact_search(self):
        search_value = self.enter_name.get()
        if search_value in self.cont:
            details = self.cont[search_value]
            self.result_label.config(text=f"Contact Details:\nName: {search_value}\nPhone: {details['Phone']}\n"
                                          f"Email: {details['Email']}\nAddress: {details['Address']}")
        else:
            self.result_label.config(text=f"Contact '{search_value}' not found.")

    def contact_update(self):
        name = self.enter_name.get()
        if name in self.cont:
            self.cont[name]['Phone'] = self.enter_phone_number.get()
            self.cont[name]['Email'] = self.enter_emailId.get()
            self.cont[name]['Address'] = self.address_entry.get()
            self.result_label.config(text=f"Contact '{name}' updated successfully.")
        else:
            self.result_label.config(text=f"Contact '{name}' not found.")

    def contact_delete(self):
        name = self.enter_name.get()
        if name in self.cont:
            del self.cont[name]
            self.result_label.config(text=f"Contact '{name}' deleted successfully.")
        else:
            self.result_label.config(text=f"Contact '{name}' not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Contact_Book(root)
    root.configure(background='Purple')
    root.mainloop()

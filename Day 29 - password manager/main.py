import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_chars = password_letters + password_symbols + password_numbers
    random.shuffle(password_chars)
    password_string = "".join(password_chars)
    pyperclip.copy(password_string)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        user_action = messagebox.askyesno(website, f"Are you sure you want to save this data?\nWebsite: {website}\nEmail:{email}\nPassword: {password}")
        if user_action:
            new_data = {website: {'email': email, 'password': password}}
            try:
                with open('data.json', 'r') as data_file:
                    json_data = json.load(data_file)
                    json_data.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=2)
            except json.decoder.JSONDecodeError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=2)
            else:
                with open('data.json', 'w') as data_file:
                    json.dump(json_data, data_file, indent=2)
            finally:
                messagebox.showinfo("Success", "Password has been added")
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

def search():
    try:
        with open('data.json', 'r') as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Password not found.")
    else:
        website = website_entry.get()
        if website in json_data:
            pass_dict = json_data[website]
            messagebox.showinfo("Success", f"Password has been found \nWebsite: {website}\nEmail:{pass_dict['email']}\nPassword: {pass_dict['password']}")
        else:
            messagebox.showinfo("Error", "Password not found.")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#fff")

# Logo
bg = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(window, width=200, height=200, bg="#fff", borderwidth=0, highlightthickness=0)
canvas.create_image(100, 100, image=bg)
canvas.grid(row=0, column=1)

website_label = tk.Label(window, text="Website:", bg="#fff", pady=10)
website_label.grid(row=1, column=0)

website_entry = tk.Entry(window, width=23)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=1)

search_btn = tk.Button(window, text="Search", command=search)
search_btn.grid(row=1, column=2)

email_label = tk.Label(window, text="Email/username:", bg="#fff", pady=10)
email_label.grid(row=2, column=0)

email_entry = tk.Entry(window, width=35)
email_entry.insert(0, "piotrkozubek@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = tk.Label(window, text="Password:", bg="#fff", pady=10)
password_label.grid(row=3, column=0)

password_entry = tk.Entry(window, width=23)
password_entry.grid(row=3, column=1)

generate_button = tk.Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", command=add_password, width=33)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

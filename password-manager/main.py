from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    password_letters = [random.choice(letters) for char in range(0, 8 + 1)]
    password_numbers = [random.choice(symbols) for char in range(0, 3 + 1)]
    password_symbols = [random.choice(numbers) for char in range(0, 3 + 1)]
    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)
    pyperclip.copy("".join(map(str, password)))
    passwordText.delete(0, END)
    passwordText.insert(0, "".join(map(str, password)))


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    name = str(websiteText.get())
    email = str(emailText.get())
    password = str(passwordText.get())
    validated = len(name) > 0 and len(email) > 0 and len(password) > 1
    if validated:
        passString = f"{name} | {email} | {password}\n"
        new_data = {name: {"email": email, "password": password}}
        try:
            with open(file="password_data.json", mode="r") as passData:
                data = json.load(passData)
        except FileNotFoundError:
            with open(file="password_data.json", mode="w") as passData:
                json.dump(new_data, passData, indent=2)
        else:
            data.update(new_data)
            with open(file="password_data.json", mode="w") as passData:
                json.dump(data, passData, indent=2)
        finally:
            websiteText.delete(0, END)
            emailText.delete(0, END)
            passwordText.delete(0, END)
            websiteText.focus()
    else:
        messagebox.showwarning(
            title="Error Validating",
            message="Please Ensure all Validation Checks are met with.",
        )


# ---------------------------- SAVE PASSWORD ------------------------------- #


def search_websites():
    try:
        with open(file="password_data.json", mode="r") as passData:
            data = json.load(passData)
    except FileNotFoundError:
        messagebox.showwarning(
            title="Error Fetching Data",
            message="You Haven't Saved any Passwords Previously",
        )
    else:
        searchText = str(websiteText.get()).lower()
        if len(searchText) > 0:
            for (key, vals) in data.items():
                if searchText == key:
                    email = vals["email"]
                    password = vals["password"]
                    messagebox.showinfo(
                        title=f"{key}",
                        message=f"You have Saved the Following Details\n Email: {email}\n Password: {password}",
                    )
        else:
            messagebox.showwarning(
                title="Error", message="Enter a Website name to Search"
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=120, pady=80)

headline = Label(
    text="Manage Your Passwords Efficiently", font=("Courier New", 15, "bold")
)
headline.grid(row=0, column=1)

canvas = Canvas(width=200, height=200, highlightthickness=0)
passPhoto = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=passPhoto)
canvas.grid(row=1, column=1)

websiteLabel = Label(text="Website: ", width=25)
websiteLabel.grid(row=2, column=0)

websiteText = Entry(width=70)
websiteText.focus()
websiteText.grid(row=2, column=1)

websiteSearch = Button(text="Search", width=15, command=search_websites)
websiteSearch.grid(row=2, column=2)

emailLabel = Label(text="Email/Username: ", width=25)
emailLabel.grid(row=3, column=0)

emailText = Entry(width=90)
emailText.insert(0, "tksudharshan@gmail.com")
emailText.grid(row=3, column=1, columnspan=2)

passwordLabel = Label(text="Password: ", width=25)
passwordLabel.grid(row=4, column=0)

passwordText = Entry(width=70)
passwordText.grid(row=4, column=1)

passwordBtn = Button(text="Generate Password", width=15, command=gen_password)
passwordBtn.grid(row=4, column=2)

addBtn = Button(text="Add", width=76, command=save_pass)
addBtn.grid(row=5, column=1, columnspan=2)

window.mainloop()

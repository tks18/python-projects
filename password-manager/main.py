# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=120, pady=80)

headline = Label(text="Manage Your Passwords Efficiently", font=("Courier New", 15, "bold"))
headline.grid(row=0, column=1)

canvas = Canvas(width=200, height=200, highlightthickness=0)
passPhoto = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=passPhoto)
canvas.grid(row=1,column=1)

websiteLabel = Label(text="Website: ", width=25)
websiteLabel.grid(row=2, column=0)

websiteText = Entry(width=90)
websiteText.grid(row=2, column=1, columnspan=2)

emailLabel = Label(text="Email/Username: ", width=25)
emailLabel.grid(row=3, column=0)

emailText = Entry(width=90)
emailText.grid(row=3, column=1, columnspan=2)

passwordLabel = Label(text="Password: ", width=25)
passwordLabel.grid(row=4, column=0)

passwordText = Entry(width=70)
passwordText.grid(row=4, column=1)

passwordBtn = Button(text="Generate Password", width=15)
passwordBtn.grid(row=4, column=2)

addBtn = Button(text="Add", width=76)
addBtn.grid(row=5, column=1, columnspan=2)

window.mainloop()
from tkinter import *
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
BLACK_COLOR = "#000000"

# Other Vars
flip_switch = False
current_card = {}

# Read Data
correct_ans = []
cards_data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

# UI
window = Tk()
window.title("Flashy...")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Generate Random Data
def gen_random_card():
    global current_card
    non_answered_data = cards_data
    for card in correct_ans:
        non_answered_data.remove(card)
    current_card = random.choice(non_answered_data)
    canvas.itemconfig(card_word, text=current_card["French"])


# Flip the Card after Set time
def flip_card():
    global flip_switch
    flip_switch = not flip_switch
    if flip_switch:
        canvas.itemconfig(card_image, image=card_back)
        canvas.itemconfig(card_title, fill=BACKGROUND_COLOR, text="English")
        canvas.itemconfig(card_word, fill=BACKGROUND_COLOR)
    else:
        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(card_title, fill=BLACK_COLOR, text="French")
        canvas.itemconfig(card_word, fill=BLACK_COLOR)
    gen_random_card()
    window.after(4000, flip_card)


# Canvas - Card
canvas = Canvas(width=805, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="images/card_front.png")
card_front = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(402, 265, image=card_front)
card_title = canvas.create_text(
    400, 150, text="French", font=("Arial", 40, "italic"), fill=BLACK_COLOR
)
card_word = canvas.create_text(
    400, 260, text="Title", font=("Arial", 60, "bold"), fill=BLACK_COLOR
)
gen_random_card()
canvas.grid(row=0, column=0, columnspan=2)

window.after(4000, flip_card)

# Buttons
yesImage = PhotoImage(file="images/right.png")
yesButton = Button(image=yesImage, command=gen_random_card)
yesButton.grid(row=1, column=0)

noImage = PhotoImage(file="images/wrong.png")
noButton = Button(image=noImage, command=gen_random_card)
noButton.grid(row=1, column=1)

window.mainloop()
from tkinter import *
from tkinter import messagebox
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
BLACK_COLOR = "#000000"

# Other Vars
flip_switch = False
current_card = {}
flip_loop = None

# Read Data
correct_ans = []
wrong_ans = []
cards_data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


# Generate Random Data
def gen_random_card():
    global current_card, correct_ans
    non_answered_data = cards_data
    for card in correct_ans:
        if card in non_answered_data:
            non_answered_data.remove(card)
    for card in wrong_ans:
        if card in non_answered_data:
            non_answered_data.remove(card)
    if len(non_answered_data) < 1:
        window.after_cancel(flip_loop)
        pandas.DataFrame(data=wrong_ans).to_csv("wrong_answers.csv")
        pandas.DataFrame(data=correct_ans).to_csv("correct_answers.csv")
        messagebox.showinfo(
            title="Success",
            message="You Have Finished all the Words, Wrong and Correct words are Saved in a Sepreate CSV Files Each",
        )
    else:
        current_card = random.choice(non_answered_data)
        canvas.itemconfig(card_word, text=current_card["French"])


# Flip the Card after Set time
def flip_card():
    global flip_switch, flip_loop
    flip_switch = not flip_switch
    if flip_switch:
        canvas.itemconfig(card_image, image=card_back)
        canvas.itemconfig(card_title, fill=BACKGROUND_COLOR, text="English")
        canvas.itemconfig(
            card_word, fill=BACKGROUND_COLOR, text=current_card["English"]
        )
    else:
        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(card_title, fill=BLACK_COLOR, text="French")
        canvas.itemconfig(card_word, fill=BLACK_COLOR)
        gen_random_card()
        flip_loop = window.after(4000, flip_card)


def add_to_list_and_flip():
    global correct_ans
    if current_card not in correct_ans:
        correct_ans.append(current_card)
    flip_card()


def remove_to_list_and_flip():
    global wrong_ans
    if current_card not in wrong_ans:
        wrong_ans.append(current_card)
    flip_card()


# UI
window = Tk()
window.title("Flashy...")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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

# Buttons
yesImage = PhotoImage(file="images/right.png")
yesButton = Button(image=yesImage, command=add_to_list_and_flip)
yesButton.grid(row=1, column=0)

noImage = PhotoImage(file="images/wrong.png")
noButton = Button(image=noImage, command=remove_to_list_and_flip)
noButton.grid(row=1, column=1)

flip_loop = window.after(4000, flip_card)

window.mainloop()

# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK="✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
checkLabelText = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    headline.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timerText, text="00:00")
    reps = 1
    checkLabel.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_secs)
        headline.config(text="Long Break", fg=RED)
    elif reps % 2 == 1:
        count_down(work_secs)
        headline.config(text="Work !", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        headline.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

import math, time

def count_down(count):
    global reps, checkLabelText, timer
    minutes = math.floor(count / 60)
    seconds = int(count % 60) 
    if seconds < 10:
        seconds = f"0{seconds}" 
    formattedText = f"{minutes}:{seconds}"
    canvas.itemconfig(timerText, text=formattedText)
    if count > 0:
       timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            checkLabelText = checkLabelText+CHECKMARK
            checkLabel.config(text=checkLabelText)
        time.sleep(0.75)
        reps += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=120, pady=60, bg=YELLOW)

headline = Label(text="Timer",fg=GREEN,font=(FONT_NAME,40,"bold"))
headline.grid(row=0,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
timerText = canvas.create_text(100, 112, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))           
canvas.grid(row=1, column=1)

startBtn = Button(text="Start", command=start_timer)
startBtn.grid(row=2,column=0)

resetBtn = Button(text="Reset", command=reset_timer)
resetBtn.grid(row=2, column=2)

checkLabel = Label(fg="#00FF00", font=(FONT_NAME,12,"bold"))
checkLabel.grid(row=3,column=1)


window.mainloop()

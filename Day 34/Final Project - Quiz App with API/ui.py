from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreboard = Label(text="Score: 0", pady=20, bg=THEME_COLOR, fg="#FFF")
        self.scoreboard.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="#FFF")
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            text="Something Something Something Something Something Something Something Something Something ",
            font=("Arial", 10, "italic"),
            fill=THEME_COLOR,
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.get_next_ques()
        tick_image = PhotoImage(file="images/true.png")
        self.correct_btn = Button(image=tick_image, pady=20, command=self.true_ans)
        self.correct_btn.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_image, pady=20, command=self.false_ans)
        self.wrong_btn.grid(row=2, column=1)
        self.window.mainloop()

    def get_next_ques(self):
        has_questions = self.brain.still_has_questions()
        if has_questions:
            q_text = self.brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.canvas_text,
                text=f"You have Reached the end of the Quiz with a Score of {self.brain.score}",
            )

    def check_answer(self, answer):
        check = self.brain.check_answer(user_answer=answer)
        if check:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.canvas_text, fill="#FFF")
            self.scoreboard.config(text=f"Score: {self.brain.score}")
            self.window.after(1000, self.revert_to_original)
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.canvas_text, fill="#FFF")
            self.scoreboard.config(text=f"Score: {self.brain.score}")
            self.window.after(1000, self.revert_to_original)

    def true_ans(self):
        self.check_answer("true")

    def false_ans(self):
        self.check_answer("false")

    def revert_to_original(self):
        self.canvas.config(bg="#FFF")
        self.canvas.itemconfig(self.canvas_text, fill=THEME_COLOR)
        self.get_next_ques()

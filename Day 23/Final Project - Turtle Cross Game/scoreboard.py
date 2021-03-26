from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.level = 1
        self.pu()
        self.goto(-250, 250)
        self.write(f"Level - {self.level}", align="left", font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level - {self.level}", align="left", font=FONT)

    def finish(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

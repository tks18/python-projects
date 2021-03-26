from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_score());
        self.color("white")
        self.speed("fastest")
        self.ht()
        self.pu()
        self.goto(0, 280)
        self.write(f"Score: {self.score} High Score: {self.high_score}",move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",move=False, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update();

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score;
            self.write_score();
        self.score = 0;
        self.update();

    def read_score(self):
        with open("high_score.txt", mode="r") as score:
            return score.read()

    def write_score(self):
        with open("high_score.txt", mode="w") as score:
            score.write(str(self.high_score))

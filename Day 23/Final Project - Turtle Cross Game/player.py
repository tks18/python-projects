from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 290


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("turtle")
        self.shapesize(1,1,2)
        self.pu()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move(self):
        getPos = self.pos();
        if(getPos[1] > FINISH_LINE_Y):
            self.finished = True;
        else:
            self.forward(MOVE_DISTANCE)

    def isFinished(self):
        getPos = self.pos();
        if(getPos[1] > FINISH_LINE_Y):
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

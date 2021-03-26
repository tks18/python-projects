from turtle import Turtle
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes = []
        self.running = False
        for n in range(3):
            newSnake = self.createSnake(-(n*20), 0)
            self.snakes.append(newSnake)
        self.head = self.snakes[0]

    def createSnake(self, x, y):
        newSnake = Turtle("square")
        newSnake.pu()
        newSnake.goto(x, y)
        newSnake.shapesize(1,1)
        newSnake.color("white")
        return newSnake

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def extend(self):
        getCors = self.getpos()
        newSnake = self.createSnake(getCors["x"], getCors["y"])
        self.snakes.append(newSnake);

    def getpos(self):
        x = self.snakes[len(self.snakes) - 1].xcor() * -20
        y = self.snakes[len(self.snakes) - 1].ycor()
        return {
            "x": x,
            "y": y
        }

    def reset(self):
        for snake in self.snakes:
            snake.goto(1002, 1000)
        self.snakes.clear()
        for n in range(3):
            newSnake = self.createSnake(-(n*20), 0)
            self.snakes.append(newSnake)
        self.head = self.snakes[0]

    def move(self):
        for cors in range(len(self.snakes)-1, 0, -1):
            newx = self.snakes[cors - 1].xcor()
            newy = self.snakes[cors - 1].ycor()
            self.snakes[cors].goto(newx, newy)
        self.snakes[0].forward(MOVE_DISTANCE)

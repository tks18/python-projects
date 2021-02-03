import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
turtle = Player();
carManager = CarManager()
scoreBoard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
screen.onkey(turtle.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move_cars()
    if carManager.checkCollision(turtle):
        scoreBoard.finish();
        game_is_on = False
    if turtle.isFinished():
        scoreBoard.update()
        carManager.incrementit()

screen.exitonclick();

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake zzzzz Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsRunning = True
while gameIsRunning:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if (snake.head.distance(food) < 15):
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if (snake.head.xcor() > 300) or (snake.head.xcor() < -300) or (snake.head.ycor() > 300) or (snake.head.ycor() < -300):
        scoreboard.reset()
        snake.reset()

    for snakes in snake.snakes[1:]:
        if snake.head.distance(snakes) < 5:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

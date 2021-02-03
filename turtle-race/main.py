import turtle
import random

screen = turtle.Screen()
screen.setup(width=700, height=600)
prefCol = screen.textinput("Make Your Bet", "Which Turtle will win, Enter a Rainbow Color")
colors = ["red", "green", "yellow", "blue", "indigo", "violet", "orange"]

summa = []
for _ in range(7):
    summa.append(turtle.Turtle("turtle"))


i = 0
j = 0
for t in summa:
    t.pu()
    t.color(colors[j])
    t.goto(x=-330, y=(-150+i))
    i += 50
    j += 1

isRaceOn = False
if prefCol:
    isRaceOn = True

while isRaceOn:
    for ts in summa:
        if ts.xcor() > 330:
            isRaceOn = False
            screen.exit()
            print(f"The winner is {ts.pencolor()}")
        ts.fd(random.randint(0, 10))

screen.exitonclick()

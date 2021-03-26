from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager():
    def __init__(self):
        self.allCars = []
        self.increment = 3
        self.startingDistance = 5
        self.chance = 5

    def create_car(self):
        randomint = random.randint(1, self.chance);
        if(randomint == 1):
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.seth(180)
            new_car.goto(300, random.randint(-250, 250))
            self.allCars.append(new_car)

    def move_cars(self):
        for cars in self.allCars:
            cars.forward(self.startingDistance)

    def checkCollision(self, turtleboy):
        for car in self.allCars:
            if(car.distance(turtleboy) < 20):
                return True;

    def incrementit(self):
        self.chance -= 1
        self.startingDistance += self.increment

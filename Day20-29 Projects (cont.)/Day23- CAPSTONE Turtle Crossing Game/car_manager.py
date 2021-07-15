from random import randint, choice
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.step = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1, 6) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.setheading(180)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.step)

    def cars_getting_faster(self):
        self.step += MOVE_INCREMENT




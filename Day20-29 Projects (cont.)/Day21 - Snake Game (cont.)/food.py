from turtle import Turtle
import random
COLOR = "DodgerBlue"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
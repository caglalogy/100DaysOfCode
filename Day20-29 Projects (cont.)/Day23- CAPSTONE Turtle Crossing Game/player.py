from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("black")
        self.shape("turtle")

    def up(self):
        self.forward(MOVE_DISTANCE)

    def car_detect(self, cars):
        for car in cars:
            if self.distance(car) < 20:
                return False
        return True

    def win(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

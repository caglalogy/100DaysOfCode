from turtle import Turtle
STEP = 20

class Player(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, y_cor)

    def move_up(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - STEP
        self.goto(self.xcor(), new_y)



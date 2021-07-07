from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.width(3)
        self.color("gray10")
        self.draw_borders()

    def draw_borders(self):
        self.penup()
        self.goto(-295, -295)
        self.pendown()
        for i in range(4):
            self.forward(590)
            self.left(90)

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def create_line(self):
        self.goto(0, 260)
        self.setheading(270)
        for i in range(-260, 260, 40):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def increase_score(self, player):
        if player == 1:
            self.p1_score += 1
        elif player == 2:
            self.p2_score += 1

    def write_scoreboard(self):
        self.goto(0, 270)
        self.setheading(0)
        self.write(f"{self.p1_score}       |       {self.p2_score}", move=False, align="center" ,font=("Sans Serif", 20, "normal" ))
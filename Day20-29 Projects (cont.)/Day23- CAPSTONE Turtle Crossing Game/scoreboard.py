from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.color("black")

    def game_over(self):
        self.write("GAME OVER", False, align="center", font=FONT)

    def win_announce(self):
        self.level += 1
        self.write("YOU WIN!\n"
                   f"LEVEL {self.level} IS COMING!", False, align="center", font=FONT)

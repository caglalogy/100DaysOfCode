from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor("black")

    def increase_score(self):
        self.score += 1

    def explanation(self):
        self.clear()
        self.write("Eat the blue turtle. \n"
                   "Use W, A, S, D.", align="center", move=False,
                   font=("Courier", 15, "normal"))
        time.sleep(3)
        self.clear()
        for i in range(3, 0, -1):
            self.write(i, align="center", move=False, font=("Courier", 15, "bold"))
            time.sleep(1)
            self.clear()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align="center", font=("Courier", 15, "bold"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\n   -{self.score}-", False, align="center", font=("Courier", 20, "normal"))
        self.hideturtle()

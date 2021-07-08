from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.01

    def refresh(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1

    def detect_player(self, player1, player2):
        if self.distance(player2) < 50 and self.xcor() > 320:
            self.x_move *= -1
            self.move_speed *= 0.9
            return 2

        if self.distance(player1) < 50 and self.xcor() < -320:
            self.x_move *= -1
            self.move_speed *= 0.9
            return 1



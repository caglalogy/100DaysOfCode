import time
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import  Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p2 = Player(350, 0)
p1 = Player(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(p1.move_up, "w")
screen.onkey(p1.move_down, "s")
screen.onkey(p2.move_up, "Up")
screen.onkey(p2.move_down, "Down")

game_is_on = True

while game_is_on:
    scoreboard.create_line()
    time.sleep(0.1)
    screen.update()
    ball.move()
    ball.detect_collision()
    ball.detect_player(p1, p2)
    if ball.xcor() < -340:
        scoreboard.increase_score(2)
        ball.refresh()
    if ball.xcor() > 340:
        scoreboard.increase_score(1)
        ball.refresh()
    scoreboard.write_scoreboard()
    scoreboard.clear()

screen.exitonclick()
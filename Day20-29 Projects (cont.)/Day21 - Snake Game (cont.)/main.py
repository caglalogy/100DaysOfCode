from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time

screen = Screen()
screen.setup(width=610, height=610)
screen.bgcolor("OliveDrab3")
screen.title("SNAKE")
screen.tracer(0)

border = Border()
snake = Snake()
food = Food()
score = Scoreboard()

game_is_on = True


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

score.explanation()

while game_is_on:
    score.write_score()
    # animation settings
    screen.update()
    time.sleep(0.07)

    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.detect_wall() or snake.detect_tail():
        game_is_on = False
        score.game_over()


screen.exitonclick()


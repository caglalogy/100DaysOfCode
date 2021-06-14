import turtle as t
import random
t.colormode(255)

cos = t.Turtle()
screen = t.Screen()
cos.speed("fastest")
cos.width(1)
angle = 5
turn = int(360/angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(turn):
    cos.color(random_color())
    cos.circle(100.0)
    cos.right(angle)

screen.exitonclick()
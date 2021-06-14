import turtle as tr
import random


t = tr.Turtle()
screen = tr.Screen()
tr.bgcolor("CadetBlue4")
t.shape("turtle")
tr.colormode(255)  # rgb colors

angles = [0, 90, 180, 270, 360]
t.width(10)
t.speed(3)


def random_direction():
    return random.randint(0, 360)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(200):
    t.pencolor(random_color())
    t.forward(30)
    # t.right(random_direction())
    t.setheading(random.choice(angles))
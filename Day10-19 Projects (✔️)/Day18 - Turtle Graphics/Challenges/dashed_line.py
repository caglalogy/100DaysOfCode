from turtle import Turtle, Screen


def start(pen, point):
    pen.penup()
    pen.sety(0)
    pen.setx(point)
    pen.pendown()


def draw_dash_line(point, space, step, repeat):
    pen = Turtle()
    screen = Screen()
    start(pen, point)
    for _ in range(repeat):
        pen.forward(step)
        pen.penup()
        pen.forward(space)
        pen.pendown()
    screen.exitonclick()


def main():
    point = int(input("Start point on x axis: "))
    step = int(input("Length of step: "))
    space = int(input("Length of step: "))
    repeat = int(input("Repeat number: "))

    draw_dash_line(point, space, step, repeat)


main()

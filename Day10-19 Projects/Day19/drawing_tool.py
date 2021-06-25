from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def func_w():
    tim.forward(30)


def func_s():
    tim.backward(30)


def func_a():
    tim.left(10)


def func_d():
    tim.right(10)


def func_c():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def func_r():
    tim.color("red")


def func_g():
    tim.color("green")


def func_b():
    tim.color("blue")


screen.onkey(key="w", fun=func_w)
screen.onkey(key="s", fun=func_s)

screen.onkey(key="a", fun=func_a)
screen.onkey(key="d", fun=func_d)
screen.onkey(key="w", fun=func_w)
screen.onkey(key="c", fun=func_c)
screen.onkey(key="r", fun=func_r)
screen.onkey(key="g", fun=func_g)
screen.onkey(key="b", fun=func_b)

screen.exitonclick()
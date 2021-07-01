from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.width(10)
t.color("hot pink")

for _ in range(5):
    t.forward(700)
    t.right(144)

screen.exitonclick()
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("green")

# drawing square 100*100
for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen.exitonclick()
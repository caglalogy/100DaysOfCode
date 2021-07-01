from turtle import Screen, Turtle
from random import randint

# screen settings
screen = Screen()
screen.title("1. Geleneksel Kaplumbağa Yarışı")
screen.setup(width=500, height=400)

bet = screen.textinput(title="GUESS", prompt="Who will be the winner? Enter a color.")

# announcer turtle writes the result on the screen at the end of the race.
announcer = Turtle()
announcer.hideturtle()

# competitor turtles
timmy = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")
benny = Turtle(shape="turtle")
jenny = Turtle(shape="turtle")
kennedy = Turtle(shape="turtle")
josh = Turtle(shape="turtle")

turtle_list = [timmy, tommy, benny, jenny, kennedy, josh]
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]


def set_turtles(turtles, colors):
    y_pos = -125
    x_pos = -230
    color_index = 0
    for t in turtles:
        t.penup()
        t.color(colors[color_index])
        t.goto(x_pos, y_pos)
        color_index += 1
        y_pos += 50


is_race_on = False
# checking if bet is given or not.
if bet:
    is_race_on = True

# race starts here
set_turtles(turtle_list, color_list)

while is_race_on:
    # turtles move randomly between 0-10 orderly.
    for turtle in turtle_list:
        turtle.forward(randint(0, 10))

    # if one of turtles passes the finish line which is defined at (230,y), race ends.
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            if winner_color == bet:
                announcer.write(f'{bet} turtle won! You won!', align='center')
                is_race_on = False
            else:
                announcer.write(f'{winner_color} turtle won! You lost.', align='center')
                is_race_on = False

screen.exitonclick()

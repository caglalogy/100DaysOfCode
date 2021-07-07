from turtle import Turtle

MOVE_DISTANCE = 20  # step length
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # positions of first tree segments at the beginning
COLOR = "black"
# heading constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segments(pos)

    def add_segments(self, pos):
        new_seg = Turtle("square")
        new_seg.color(COLOR)
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    # snakes move in a while loop on main.py, so we just change the direction
    def move(self):
        for seg_n in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_n - 1].xcor()
            new_y = self.segments[seg_n - 1].ycor()
            self.segments[seg_n].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # press key functions for up, down, right and left
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def detect_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True

    def detect_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

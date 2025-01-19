from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    body = []
    head = None
    def __init__(self):
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset_snake(self):

        for seg in self.body:
            seg.reset()

        self.body.clear()
        for position in STARTING_POSITIONS:
            self.add_segment(position)

        self.head = self.body[0]

    def add_segment(self, position):
        turtle = Turtle()
        turtle.color("white")
        turtle.shape("square")
        turtle.penup()
        turtle.goto(position)
        self.body.append(turtle)

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            position = self.body[seg_num - 1].position()
            self.body[seg_num].goto(position)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        print("Going Up", self.head.heading())
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        print("Going Down")
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        print("Turning Left")
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        print("Turning Right")
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        print("Growing")
        self.add_segment(self.body[-1].position())


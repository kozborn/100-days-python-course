from turtle import Turtle

POSITIONS = [-50, -30, -10, 10, 30]

class Paddle():
    def __init__(self):

        self.paddle = []
        for position in POSITIONS:
            sq = Turtle()
            sq.shape("square")
            sq.color("white")
            sq.penup()
            sq.goto((350, position))
            self.paddle.append(sq)

    def go_up(self):
        if self.paddle[-1].ycor() < 280:
            for t in self.paddle:
                t.goto((t.xcor(), t.ycor() + 20))


    def go_down(self):
        if self.paddle[0].ycor() > -280:
            for t in self.paddle:
                t.goto((t.xcor(), t.ycor() - 20))

class Paddle2(Turtle):
    def __init__(self, x = 0, y = 0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto((x, y))
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() < 250:
            self.goto((self.xcor(), self.ycor() + 20))


    def go_down(self):
        if self.ycor() > -250:
            self.goto((self.xcor(), self.ycor() - 20))


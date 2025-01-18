from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = [0, 0]
        self.color("white")
        self.penup()
        self.redraw()
        self.hideturtle()


    def increase_score(self, index):
        self.scores[index] += 1
        self.redraw()

    def redraw(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"{self.scores[0]} : {self.scores[1]}", False, align="center", font=FONT)
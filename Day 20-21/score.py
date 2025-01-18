from turtle import Turtle

FONT = ("Arial", 20, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.redraw()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.redraw()

    def redraw(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=FONT)

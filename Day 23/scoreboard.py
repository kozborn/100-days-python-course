from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-360, 260)
        self.draw()

    def draw(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.draw()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


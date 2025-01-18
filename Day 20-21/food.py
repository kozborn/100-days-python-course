from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(random.randint(-390, 390), random.randint(-290, 290))

    def refresh(self):
        self.goto(random.randint(-390, 390), random.randint(-290, 290))
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self, screen_height):
        self.cars = []
        self.add_car()
        self.speed = STARTING_MOVE_DISTANCE
        self.levels = [1]

    def add_car(self):
        if (random.randint(1, 6) == 1):
            t = Turtle()
            t.penup()
            t.shape("square")
            t.shapesize(stretch_len=2)
            t.color(random.choice(COLORS))
            t.setheading(180)
            t.goto(400, random.randint(-250, 250))
            self.cars.append(t)

    def update(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -400:
                self.cars.remove(car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT






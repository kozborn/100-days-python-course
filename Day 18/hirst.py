import colorgram
import turtle as T
from turtle import Screen
import random

T.colormode(255)
alice = T.Turtle()
alice.shape("turtle")
alice.color("pink")

colors = colorgram.extract("./image.jpg", 20)

color_tuples = []
for color in colors:
    color_tuples.append((color.rgb[0], color.rgb[1], color.rgb[2]))


print(color_tuples)
rgb_colors = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157)]
alice.speed("fastest")
alice.penup()
alice.setposition(x=-380, y=-270)
alice.pendown()
for y in range(10):
    for x in range(10):
        alice.dot(20)
        alice.penup()
        alice.color(random.choice(color_tuples))
        alice.forward(60)

    alice.penup()
    alice.setposition(x=-380, y=-270 + (y + 1) * 50)
    alice.pendown()

screen = Screen()
screen.colormode(255)
screen.exitonclick()
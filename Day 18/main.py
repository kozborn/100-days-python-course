import heroes
import turtle as T
from turtle import Screen
import random
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("medium aquamarine")
#

T.colormode(255)
alice = T.Turtle()
alice.shape("turtle")
alice.color("pink")

def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# draw_square(timmy)
#
# alice.setposition(10, 10)
# draw_square(alice)


colors = [
    "#1A73E8", "#34A853", "#FBBC05", "#EA4335", "#FF5733",
    "#33FF57", "#5733FF", "#FFC300", "#DAF7A6", "#900C3F",
    "#581845", "#C70039", "#900C3F", "#FF5733", "#33FFBD",
    "#8E44AD", "#16A085", "#2ECC71", "#3498DB", "#E74C3C"
]

# for i in range(len(colors)):
#     t = Turtle()
#     t.shape("turtle")
#     t.color(colors[i])
#     t.setposition(i * 10, i * 10)
#     draw_square(t)

alice.color(colors[0])
# for _ in range(10):
#     alice.pendown()
#     alice.forward(10)
#     alice.penup()
#     alice.forward(10)
#
# alice.pendown()

directions = [0, 90, 180, 270]

alice.width(2)
alice.speed("fastest")

def random_color():
    return (random.randint(0, 255), random.randint(0, 255)  , random.randint(0, 255))

gap = 5

for i in range(int(360/gap)):
    color = random_color()
    alice.color(color)
    alice.circle(200)
    alice.setheading(alice.heading() + gap)

for _ in range(10):
    color = random_color()
    print(color)
    alice.forward(30)

    alice.color(random_color())
    alice.setheading(random.choice(directions))
#
#
# def draw_shape(num_of_sides):
#     for line in range(num_of_sides):
#         alice.forward(40)
#         alice.right(int(360 / num_of_sides))
#
# for num_of_sides in range(3, 11):
#     alice.color(colors[num_of_sides])
#     draw_shape(num_of_sides)



# for _ in range(100):
#     print(heroes.gen())

























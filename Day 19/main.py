from turtle import Turtle, Screen

alice = Turtle()


def move_forward():
    alice.forward(10)

def move_backward():
    alice.backward(10)

def rotate_left():
    alice.left(10)

def rotate_right():
    alice.right(10)

def clear_screen():
    screen.resetscreen()

screen = Screen()   
screen.listen()
screen.onkey(clear_screen, "c")
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(rotate_left, "Left")
screen.onkey(rotate_right, "Right")

screen.exitonclick()

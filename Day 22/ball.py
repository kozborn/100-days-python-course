from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.05
        self.y_direction = 1
        self.x_direction = 1
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5


    # def move(self):
    #     self.setheading(45)
    #     self.forward(20)

    def increase_speed(self):
        self.move_speed *= 0.75

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_y()
        self.bounce_x()





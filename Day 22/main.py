from turtle import Turtle, Screen
from paddle import Paddle2
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle2(350, 0)
left_paddle = Paddle2(-350, 0)
screen.update()
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
is_game_on = True

ball = Ball()
scoreboard = Scoreboard()

while is_game_on:
    time.sleep(ball.move_speed)
    if ball.xcor() > 380:
        scoreboard.increase_score(0)
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.increase_score(1)
        ball.reset_position()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50:
            ball.bounce_x()
            ball.increase_speed()

    ball.move()
    screen.update()

screen.exitonclick()

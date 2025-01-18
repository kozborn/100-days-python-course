from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
f = Food()
s = Score()

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision detect

    if snake.head.distance(f) < 15:
        f.refresh()
        s.increase_score()
        snake.grow()

    # wall collision detect

    if snake.head.xcor() > (SCREEN_WIDTH / 2) - 10  or snake.head.xcor() < -(SCREEN_WIDTH / 2) - 10 or snake.head.ycor() > (SCREEN_HEIGHT / 2) - 10 or snake.head.ycor() < -(SCREEN_HEIGHT / 2) - 10:
        game_is_on = False
        s.game_over()

    # detect collision with tail
    for segment in snake.body[2:]:
        if snake.head.distance(segment) < 10:
            s.game_over()
            game_is_on = False






screen.exitonclick()

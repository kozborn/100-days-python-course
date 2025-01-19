import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

p = Player()
s = Scoreboard()
cm = CarManager(screen_height=SCREEN_HEIGHT)
screen.listen()
screen.onkey(p.move_up, "Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    cm.update()
    cm.add_car()
    screen.update()

    # car collision detect
    for c in cm.cars:
        if p.distance(c) < 20:
            game_is_on = False
            s.game_over()

    # screen edge detect
    if p.ycor() > int(SCREEN_HEIGHT/ 2):
        s.increase_score()
        cm.increase_speed()
        p.reset()

screen.exitonclick()

import turtle
import random

# Initialize screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -100)
ball.dx = 3  # Horizontal speed
ball.dy = 3  # Vertical speed

# Bricks
colors = ["red", "orange", "yellow", "green", "blue"]
bricks = []

for row in range(5):
    for col in range(12):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(-350 + col * 70, 250 - row * 30)
        bricks.append(brick)

# Score
score = 0
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))


# Paddle movement
def move_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 20)


def move_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 20)


# Keyboard bindings
screen.listen()
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")


# Improved collision detection
def check_collision():
    global score, ball
    # Paddle collision
    if (-260 < ball.ycor() < -240) and (
        paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60
    ):
        ball.dy *= -1
        # Add horizontal bounce variation
        ball.dx += random.uniform(-0.5, 0.5)

    # Brick collision
    for brick in bricks:
        if (
            brick.isvisible()
            and (abs(ball.xcor() - brick.xcor()) < 35)
            and (abs(ball.ycor() - brick.ycor()) < 20)
        ):
            brick.hideturtle()
            score += 10
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
            ball.dy *= -1
            break


# Game loop
def update():
    global ball
    screen.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collisions
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:  # Bottom wall
        ball.goto(0, -100)
        ball.dx = 3
        ball.dy = 3

    check_collision()

    # Win condition
    if all(not brick.isvisible() for brick in bricks):
        pen.goto(0, 0)
        pen.write("YOU WIN!", align="center", font=("Courier", 36, "bold"))
        return

    screen.ontimer(update, 10)


update()
screen.mainloop()

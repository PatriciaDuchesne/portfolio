import time
import turtle

from paddle import Paddle
from ball import Ball
from brick import Brick


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -270))
ball = Ball()
bricks = []

# Spawn bricks
x_position = -345
y_position = 275

for row in range(0, 6):
    for col in range(0, 8):
        bricks.append(Brick(f"brick{row + 1}x{col + 1}", x_position, y_position))
        x_position += 97
    x_position = -345
    y_position -= 40

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with paddle
    if ball.ycor() <= -260:
        if ball.distance(paddle) < 60:
            ball.bounce_up_or_down()

    # Detect collision with wall
    if ball.xcor() >= 385 or ball.xcor() <= -385:
        ball.bounce_on_wall()

    # Detect collision with ceiling
    if ball.ycor() >= 285:
        ball.bounce_up_or_down()

    # Detect if ball is out of bounds
    if ball.ycor() <= -310:
        # print("Game over.")
        turtle.color('white')
        turtle.write("Game over.", move=False, font=('Courier', 36, 'bold'), align='center')
        game_is_on = False

    # Detect collision with brick
    for brick in bricks:
        if ball.distance(brick) < 40:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce_up_or_down()

    if len(bricks) == 0:
        ball.hideturtle()
        time.sleep(0.25)
        turtle.color('white')
        turtle.write("You win.", move=False, font=('Courier', 36, 'bold'), align='center')
        game_is_on = False

screen.mainloop()
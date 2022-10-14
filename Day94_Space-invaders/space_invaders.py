import time
from turtle import Screen

from barrier import Barrier
from invader import Invader
from projectile import Projectile
from ship import Ship


def fire_projectile():
    x, y = ship.position()
    if not projectile.visible:
        projectile.setposition(x, y)
        projectile.showturtle()
        projectile.move()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.register_shape('./img/invader1.gif')
screen.tracer(0)
screen.listen()

ship = Ship()
projectile = Projectile()
invaders = []
barriers = []

# Spawn invaders
x_position = -195
y_position = 225
for row in range(0, 4):
    for col in range(0, 8):
        invaders.append(Invader(f"invader{col + 1}x{row + 1}", x_position, y_position))
        x_position += 55
    x_position = -195
    y_position -= 35

# Spawn barriers
# x_position_barrier = -260
# y_position_barrier = -100
# for barrier in range(0, 4):
#     for row in range(0, 4):
#         for col in range(0, 12):
#             barriers.append(Barrier(f"barrier{col + 1}x{row + 1}", x_position_barrier, y_position_barrier))
#             x_position_barrier += 6
#         x_position_barrier -= 72
#         y_position_barrier -= 6
#     x_position_barrier += 150
#     y_position_barrier = -100


screen.onkey(ship.move_left, "Left")
screen.onkey(ship.move_right, "Right")
screen.onkey(fire_projectile, "space")

game_is_on = True
nb_of_bounces = 0

while game_is_on:
    time.sleep(0.03)
    screen.update()

    # Check for remaining invaders
    if len(invaders) == 0:
        game_is_on = False
        win_message = Invader("x", 0, 0)
        win_message.player_wins()

    # Move invaders
    right_edge = 0
    left_edge = 0
    lower_edge = 0
    for invader in invaders:
        if invader.xcor() > right_edge:
            right_edge = invader.xcor()
        if invader.xcor() < left_edge:
            left_edge = invader.xcor()
        if invader.ycor() < lower_edge:
            lower_edge = invader.ycor()
    if right_edge > 330 or left_edge < -330:
        nb_of_bounces += 1
        if nb_of_bounces % 2 == 0:
            for invader in invaders:
                invader.lower()
        for invader in invaders:
            invader.shift_direction()
    for invader in invaders:
        invader.move()

    # Move projectile
    if projectile.visible:
        projectile.move()

    # Detect collision with barrier
    # for barrier in barriers:
    #     if projectile.distance(barrier) < 8:
    #         barrier.hideturtle()
    #         barriers.remove(barrier)
    #         projectile.reinit()

    # Detect ship collision with invader
    for invader in invaders:
        if ship.distance(invader) < 25 or lower_edge <= -230:
            ship.hideturtle()
            game_is_on = False
            lose_message = Invader("x", 0, 0)
            lose_message.player_loses()

    # Detect projectile collision with invader
    for invader in invaders:
        if projectile.distance(invader) < 20:
            invader.hideturtle()
            invaders.remove(invader)
            projectile.reinit()

    # Detect out of bounds projectile
    if projectile.ycor() > 310:
        projectile.reinit()

screen.mainloop()

from turtle import Screen, Turtle


class Invader(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__(shape="turtle")
        self.color("red")
        self.penup()
        self.setposition(xcor, ycor)
        self.tilt(-90)
        self.speed('slow')

        self.hit = 0


class Bullet(Turtle):
    def __init__(self):
        super().__init__(shape="arrow", visible=False)
        self.shapesize(.5, 1)
        self.color("yellow")
        self.penup()
        self.setheading(90)
        self.speed('fastest')

        self.bullet_speed = 20


def move_right():
    if player.xcor() + player_speed < 210:
        player.forward(player_speed)


def move_left():
    if player.xcor() - player_speed > -210:
        player.backward(player_speed)


def bullet_movement():
    firedb.forward(10)

    if firedb.ycor() > 195:
        firedb.hideturtle()


def fire_bullet():
    if not firedb.isvisible():
        x, y = player.position()
        firedb.setposition(x, y + 20)
        firedb.showturtle()


def isCollision(t1, t2):
    return t1.distance(t2) < 20


def move():
    global enemy_speed

    if firedb.isvisible():
        bullet_movement()

    for invader in enemies:
        if firedb.isvisible() and isCollision(firedb, invader):
            invader.hit += 1

            if invader.hit == 1:
                invader.color("orange")
            elif invader.hit == 2:
                invader.color("yellow")
            elif invader.hit == 3:
                invader.hideturtle()
                enemies.remove(invader)

            firedb.hideturtle()  # only one hit per bullet!

        invader.forward(enemy_speed)

        if invader.xcor() < -200 or invader.xcor() > 200:
            for invader in enemies:
                y = invader.ycor() - 40
                invader.sety(y)
            enemy_speed *= -1

    win.update()
    win.ontimer(move, 50)


# Player
player = Turtle("arrow")
player.color("white")
player.penup()
player.tilt(90)
player.sety(-175)
player.speed('fast')

# Window
win = Screen()
win.bgcolor("black")
win.tracer(False)

border_pen = Turtle(visible=False)
border_pen.speed('fastest')
border_pen.color("white")
border_pen.pensize(3)

border_pen.penup()
border_pen.setposition(-225, -225)
border_pen.pendown()

for _ in range(4):
    border_pen.forward(450)
    border_pen.left(90)

# Bullet
firedb = Bullet()

enemies = []

xx = -175
xxxx = -190
for invader_count in range(19):
    if invader_count < 9:
        enemies.append(Invader(xx, 200))
        xx += 30
    else:
        enemies.append(Invader(xxxx, 175))
        xxxx += 30

player_speed = 7
enemy_speed = 2

win.onkey(move_left, "Left")
win.onkey(move_right, "Right")
win.onkey(fire_bullet, "space")
win.listen()

move()

win.mainloop()

from turtle import Turtle


class Projectile(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.color("Tomato")
        self.turtlesize(0.25, 0.25)
        self.visible = False

    def move(self):
        self.setheading(90)
        self.showturtle()
        self.visible = True
        self.forward(15)

    def reinit(self):
        self.visible = False
        self.hideturtle()
        self.setposition(1000, 1000)

    def destroy(self):
        self.visible = False
        self.destroy()

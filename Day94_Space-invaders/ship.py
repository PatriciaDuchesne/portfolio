from turtle import Turtle


class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("arrow")
        self.setheading(90)
        self.color("LawnGreen")
        self.penup()
        self.setposition(0, -230)
        self.showturtle()

    def move_left(self):
        new_x = self.xcor() - 25
        self.setposition(new_x, self.ycor())
        if new_x <= -375:
            self.setx(-375)

    def move_right(self):
        new_x = self.xcor() + 25
        self.setposition(new_x, self.ycor())
        if new_x >= 375:
            self.setx(375)

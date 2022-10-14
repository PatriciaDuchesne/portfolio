from turtle import Turtle


class Barrier(Turtle):
    def __init__(self, name, x_position, y_position):
        super().__init__()
        self.name = name
        self.hideturtle()
        self.penup()
        self.setposition(x_position, y_position)
        self.shape("square")
        self.color("FloralWhite")
        self.turtlesize(0.25, 0.25)
        self.showturtle()

    def create(self):
        pass



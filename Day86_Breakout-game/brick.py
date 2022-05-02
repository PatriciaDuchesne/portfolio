from turtle import Turtle


class Brick(Turtle):

    def __init__(self, name, x_position, y_position):
        super().__init__()
        self.name = name
        self.position = (x_position, y_position)
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=4.4)
        self.color("white")
        self.penup()
        self.setposition(self.position)

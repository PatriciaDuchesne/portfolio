from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.x_move = 10
        self.y_move = -10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)

    def bounce_up_or_down(self):
        self.y_move *= -1

    def bounce_on_wall(self):
        self.x_move *= -1

from turtle import Turtle


class Invader(Turtle):
    def __init__(self, name, x_position, y_position):
        super().__init__()
        self.name = name
        self.x_move = 3
        self.penup()
        self.hideturtle()
        self.shape('./img/invader1.gif')
        self.setposition(x_position, y_position)
        self.showturtle()

    def move(self):
        new_x = self.xcor() + self.x_move
        self.setposition(new_x, self.ycor())

    def lower(self):
        new_y = self.ycor() - 35
        self.setposition(self.xcor(), new_y)

    def shift_direction(self):
        self.x_move *= -1

    def player_wins(self):
        self.color("FloralWhite")
        self.write("You win!", font=("Lucida Console", 30, "bold"), align="center")

    def player_loses(self):
        self.color("FloralWhite")
        self.write("You lose.", font=("Lucida Console", 30, "bold"), align="center")

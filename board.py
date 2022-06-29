from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()

    def create_board(self):
        self.hideturtle()
        self.penup()
        self.setposition(-350, 290)
        self.pendown()
        self.color('yellow')
        self.pensize(2)
        self.forward(700)
        self.penup()
        self.setposition(-350, -290)
        self.pendown()
        self.forward(700)
        self.color('red')
        self.setheading(90)
        self.dotted(300)
        self.penup()
        self.setposition(-350, -290)
        self.pendown()
        self.dotted(300)

    def dotted(self, distance):
        for _ in range(int(distance/20)):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()

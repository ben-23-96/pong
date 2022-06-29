from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.penup()
        self.resizemode("user")
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4, stretch_len=1)
        if self.player == 'p1':
            x = -350
        elif self.player == 'p2':
            x = 350
        self.setposition((x, 0))

    def move_upwards(self):
        y = self.ycor()
        if y <= 250:
            self.setposition((self.xcor(), y+25))

    def move_downwards(self):
        y = self.ycor()
        if y >= -250:
            self.setposition((self.xcor(), y-25))

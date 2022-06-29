from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.y_move = 10
        self.x_move = 10
        self.paddle_hits = 1

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.setposition((x + self.x_move, y + self.y_move))

    def roof_bounce(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_move = -self.y_move

    def paddle_bounce(self, paddle_position):
        if self.xcor() == 340 or self.xcor() == -340:
            if self.ycor() < paddle_position + 50 and self.ycor() > paddle_position - 50:
                self.x_move = -self.x_move
                self.paddle_hits += 1

    def rally(self):
        if self.paddle_hits == 5:
            self.paddle_hits = 0
            return True

    def goal(self):
        if self.xcor() >= 360 or self.xcor() <= -360:
            return True

    def reset(self):
        self.setposition((0, 0))
        self.x_move = -self.x_move

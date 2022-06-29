from turtle import Turtle


class Score(Turtle):
    def __init__(self, player_1, player_2):
        super().__init__()
        self.player_left_score = 0
        self.player_right_score = 0
        self.player_1 = player_1
        self.player_2 = player_2

    def add_point(self, ball_position):
        if ball_position > 0:
            self.player_left_score += 1
        elif ball_position < 0:
            self.player_right_score += 1

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color('blue')
        self.setposition((0, 290))
        self.write(f'{self.player_1} {self.player_left_score} : {self.player_2} {self.player_right_score}',
                   font=('comic sans', 20, 'bold'), align='center')

    def winner(self):
        if (self.player_left_score >= 10 and self.player_left_score - 2 >= self.player_right_score) or\
                (self.player_right_score >= 10 and self.player_right_score - 2 >= self.player_left_score):
            if self.player_left_score > self.player_right_score:
                winner = self.player_1
            else:
                winner = self.player_2
            self.color('blue')
            self.setposition((0, 0))
            self.write(f'{winner} wins!!!',
                       font=('comic sans', 20, 'bold'), align='center')
            return True

    def new_game(self):
        self.player_left_score = 0
        self.player_right_score = 0

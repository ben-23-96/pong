from turtle import Screen, done
import time
from pong_paddle import Paddle
from board import Board
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

player_left_name = screen.textinput(
    "Player 1", "Enter your name:  ")
player_right_name = screen.textinput(
    "Player 2", "Enter your name:  ")

board = Board()
board.create_board()
ball = Ball()
score = Score(player_left_name, player_right_name)


player_left = Paddle('p1')
player_right = Paddle('p2')

screen.onkeypress(player_left.move_upwards, 'w')
screen.onkeypress(player_left.move_downwards, 's')
screen.onkeypress(player_right.move_upwards, 'Up')
screen.onkeypress(player_right.move_downwards, 'Down')

game_finished = False
speed = 0.05


while not game_finished:
    screen.listen()
    screen.update()
    time.sleep(speed)

    score.write_score()

    ball.move()
    ball.roof_bounce()
    if ball.xcor() > 0:
        ball.paddle_bounce(player_right.ycor())
    elif ball.xcor() < 0:
        ball.paddle_bounce(player_left.ycor())

    if ball.rally():
        if speed > 0.01:
            speed -= 0.01

    if ball.goal():
        score.add_point(ball.xcor())
        speed = 0.05
        if score.winner():
            new_game = screen.textinput(
                "New Game", "Type yes or no for new game:  ")
            if new_game == 'yes':
                ball.reset()
                score.new_game()
            else:
                game_finished = True
        else:
            ball.reset()


done()

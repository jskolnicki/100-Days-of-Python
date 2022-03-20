import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time
import os
import random

screen = turtle.Screen()
currentDir = os.getcwd()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
screen.listen()


os.chdir(os.path.dirname(__file__))
screen.addshape(f"lordbiz.gif")

player1 = Paddle('left')
player2 = Paddle('right')
ball = Ball()

p1_scoreboard = Scoreboard(-100)
p2_scoreboard = Scoreboard(100)
#games = screen.textinput(title="Set the Rules", prompt="How many games do you want to play to? Games: ")



screen.onkey(key="q", fun= player1.move_up)
screen.onkey(key="a", fun= player1.move_down)
screen.onkey(key="Up", fun= player2.move_up)
screen.onkey(key="Down", fun= player2.move_down)



series_is_on = True
game_is_on = True



while p1_scoreboard.score < 3 and p2_scoreboard.score < 3:
    print(p1_scoreboard.score)
    print(p2_scoreboard.score)
    game_is_on = True
    player1.reset()
    player2.reset()
    ball.reset()
    screen.update()
    time.sleep(3)
    while game_is_on:
        screen.update()
        time.sleep(ball.ball_speed)

        ball.move_forward()

        if ball.pos()[1] > 280:
            ball.setposition(ball.pos()[0], 280)
            ball.hits_wall()
        if ball.pos()[1] < -280:
            ball.setposition(ball.pos()[0], -280)
            ball.hits_wall()


        if ball.pos()[0] >= 358:
            ball.setposition(358, ball.pos()[1])
            if ball.distance(player2) <= 54.626 and ball.ball_direction() == "right": #pythagorean theorem for (380-358)^2 + 50^2 = c^2
                ball.hits_paddle()
            else:
                while ball.pos()[0] < 370:
                    ball.move_forward()
                    screen.update()
                    time.sleep(.1)
                    if ball.pos()[0] > 370:
                        ball.setposition(370, ball.pos()[1])
                        game_is_on = False
                        p1_scoreboard.increase_score()

        if ball.pos()[0] <= -358:
            ball.setposition(-358, ball.pos()[1])
            if ball.distance(player1) <= 54.626 and ball.ball_direction() == 'left':
                ball.hits_paddle()
            else:
                while ball.pos()[0] > -370:
                    ball.move_forward()
                    screen.update()
                    time.sleep(.1)
                    if ball.pos()[0] < -370:
                        ball.setposition(-370, ball.pos()[1])
                        game_is_on = False
                        p2_scoreboard.increase_score()

p1_scoreboard.game_over(p1_scoreboard.score, p2_scoreboard.score)


screen.exitonclick()
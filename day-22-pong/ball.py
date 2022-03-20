from turtle import Turtle
import random
import os

SPEED = 20
STARTING_DELAY = .10

os.chdir(os.path.dirname(__file__))


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('lordbiz.gif')
        self.ball_speed = STARTING_DELAY
        self.penup()
        self.shapesize(stretch_wid = .5, stretch_len = .5)
        self.setheading((random.randint(120,150) + random.choice([90,-90, 180, 0])) % 360)

    def move_forward(self):
        self.forward(SPEED)

    def hits_wall(self):
        self.setheading(360 - self.heading())

    def hits_end(self):
        pass

    def hits_paddle(self):
        self.setheading((540 - self.heading() % 360))
        self.ball_speed *= .85

    def ball_direction(self):
        if self.heading() >= 0 and self.heading() < 90:
            return "right"
        if self.heading() <= 360 and self.heading() > 270:
            return "right"
        if self.heading() > 90 and self.heading() < 270:
            return "left"

    def reset(self):
        self.setposition(0,0)
        self.ball_speed = STARTING_DELAY
        self.setheading((random.randint(120,240) + random.choice([0,180])) % 360)
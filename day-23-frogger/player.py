from turtle import Turtle, clear
import os
import time

os.chdir(os.path.dirname(__file__))

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TEXT_ALIGNMENT = 'center'
FONT = ("Courier", 14, "normal")

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('lordbiz.gif')
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)
        self.penup()

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.setposition(STARTING_POSITION)

    def check_if_complete(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False


from turtle import Turtle
import random
import os

os.chdir(os.path.dirname(__file__))

height = 600
width = 600

FOOD_POSITIONS = []
for wide in range(1, int(width/20)):
    for tall in range(1, int(height/20)):
        FOOD_POSITIONS.append((wide*20 - int(height/2), tall * 20 - int(height/2)))


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape("lordbiz.gif")
        self.shapesize(stretch_wid = .5, stretch_len = .5)
        self.speed('fastest')
        self.setposition(random.choice(FOOD_POSITIONS))
        
    def refresh(self, turtle_positions_list):
        possible_food_positions = [e for e in FOOD_POSITIONS if e not in turtle_positions_list]
        self.setposition(random.choice(possible_food_positions))        
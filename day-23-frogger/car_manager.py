import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MOVE_INCREASE = 2
RANDOM_CHANCE = 5 # the lower the more difficult



class CarManager():
    def __init__(self):
        """Creates a random car and adds it to a list of cars"""
        self.car_list = []
        self.levels_completed = 0

    def create_car(self):
        global RANDOM_CHANCE
        if RANDOM_CHANCE != 1 and self.levels_completed % 4:
            RANDOM_CHANCE -= 1
        if random.randint(1,RANDOM_CHANCE) == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(1,2,1)
            new_car.speed('fastest')
            new_car.setheading(180)
            new_car.setposition(280, random.randint(-250,250))
            self.car_list.append(new_car)

    def drive(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT + MOVE_INCREASE * self.levels_completed)

    def find_positions(self):
        positions = []
        for position in self.car_list:
            positions.append(position.pos())
        return positions

    def reset(self):
        for car in self.car_list:
            car.reset()
            car.hideturtle()
        self.car_list = []

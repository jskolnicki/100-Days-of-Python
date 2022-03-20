import time
import os
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


os.chdir(os.path.dirname(__file__))

FONT = ("Courier", 14, "normal")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.addshape("lordbiz.gif")


player = Player()


scoreboard = Scoreboard()
car_manager = CarManager()





screen.onkey(key="Up", fun = player.move_up)
screen.onkey(key="Right", fun = player.move_right)
screen.onkey(key="Left", fun = player.move_left)




def cheat_code():
    global next_level
    next_level = True
    car_manager.levels_completed += 1
    scoreboard.level_up()
    
screen.onkey(key="space", fun = cheat_code)

def move_down():
    text = Turtle()
    text.color("black")
    text.penup()
    text.setposition(0,-290)
    text.write("There is no turning back now...", False, align= 'center', font=FONT)
    screen.ontimer(text.clear, 1500)
screen.onkey(key="Down", fun = move_down)


car_manager=CarManager()

alive = True

while alive:
    player.reset()
    #car_manager.reset()
    next_level = False
    while not next_level and alive:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.drive()
        for car in car_manager.car_list:
            if player.distance(car) < 20:
                scoreboard.game_over()
                alive = False
                break
        if player.check_if_complete():
            next_level = True
            car_manager.levels_completed += 1
            scoreboard.level_up()

            
screen.exitonclick()
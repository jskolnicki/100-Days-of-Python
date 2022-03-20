import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import os

screen = turtle.Screen()


screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")

screen.tracer(0)
screen.listen()

os.chdir(os.path.dirname(__file__))

screen.addshape("lordbiz.gif")



snake = Snake()
food = Food()
scoreboard = Scoreboard()

df = pd.DataFrame(myData)

df.head()

snake.number_of_tails = 33

print(snake.number_of_tails + 10)

screen.onkey(key="Up", fun= snake.move_up)
screen.onkey(key="Right", fun= snake.move_right)
screen.onkey(key="Left", fun= snake.move_left)
screen.onkey(key="Down", fun= snake.move_down)


series_is_on = True
game_is_on = True

while series_is_on:
        
    while game_is_on:
        
        screen.update()
        time.sleep(.1)
        snake.move()

        if snake.head.distance(food) <= 1:
            snake.add_tail()
            scoreboard.increase_score()
            food.refresh(snake.find_positions())

        #handling snake boundaries
        if snake.head.pos()[0] > 280:
            snake.head.setposition(-280, snake.head.pos()[1])
        elif snake.head.pos()[0] < -280:
            snake.head.setposition(280, snake.head.pos()[1])
        elif snake.head.pos()[1] < -280:
            snake.head.setposition(snake.head.pos()[0], 280)
        elif snake.head.pos()[1] > 280:
            snake.head.setposition(snake.head.pos()[0], -280)

        if abs(snake.head.pos()[1]) >= 300:
            snake.head.setposition(snake.head.pos()[0], snake.head.pos()[1]*-1)

        if snake.head.pos() in snake.find_positions()[1:]:
            scoreboard.game_over()
            game_is_on = False



    screen.exitonclick()
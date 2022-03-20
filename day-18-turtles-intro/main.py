from turtle import Turtle
from turtle import Screen
import random

timmy = Turtle()
screen = Screen()



timmy.shape("turtle")
timmy.color("red")


screen.colormode(255)

#Challenge 3 - triangle, square, ... , decagon
# for num in range(3,11):
#     for i in range(num):        
#         timmy.forward(100)
#         timmy.right(360/num)
#     random_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
#     timmy.pencolor(random_color)

# #Challenge 4 - Random Walk
# def is_in_screen(the_window, the_turtle):
#     left_bound = -(the_window.window_width() / 2)
#     right_bound = the_window.window_width() / 2
#     top_bound = the_window.window_height() / 2
#     bottom_bound = -(the_window.window_height() / 2)

#     turtle_x = the_turtle.xcor()
#     turtle_y = the_turtle.ycor()

#     still_in = True
#     if turtle_x > right_bound or turtle_x < left_bound:
#         still_in = False
#     if turtle_y > top_bound or turtle_y < bottom_bound:
#         still_in = False

#     return still_in

# timmy.width(10)
# timmy.speed(10)
# while is_in_screen(screen,timmy):
#     timmy.left(random.choice([0,90,180,270]))
#     timmy.forward(80)
#     random_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
#     timmy.pencolor(random_color)


# #Challenge 5 - Spirograph

# timmy.speed(10)

# turn_degrees = 10
# for i in range(round(360/10)):
#     random_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
#     timmy.pencolor(random_color)
#     timmy.circle(100)
#     timmy.left(turn_degrees)
    


#Challenge 6 - Contemporary Art


import colorgram

colors = colorgram.extract('D:/Downloads/hirst.png',25)

list_of_colors = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    list_of_colors.append((r,g,b))


del list_of_colors[:5]


timmy.penup()
starting_x = -250
starting_y = -250


for i in range(10):
    timmy.setposition(starting_x, starting_y)
    for i in range(10):
        timmy.dot(25,random.choice(list_of_colors))
        timmy.forward(50)
    starting_y += 50

timmy.hideturtle()
screen.exitonclick()
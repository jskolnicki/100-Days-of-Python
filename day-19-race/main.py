import turtle

tim = turtle.Turtle()

screen = turtle.Screen()

def move_forwards():
    tim.forward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def move_backwards():
    tim.backward(10)

def clear():
    tim.clear()
    

screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.onkey(key="Left", fun= turn_left)
screen.onkey(key='Right',fun= turn_right)
screen.onkey(key='comma',fun=move_backwards)
screen.onkey(key='c',fun=clear)

screen.exitonclick()
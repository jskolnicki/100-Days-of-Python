import turtle
import random
import os

def turtle_in_lead(list_of_turtles, list_of_turtles_str):
    x_coordinates = []
    for turtle in list_of_turtles:
        x_coordinates.append(turtle.xcor())
    max_index = x_coordinates.index(max(x_coordinates))
    return list_of_turtles_str[max_index]


screen = turtle.Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Get Your Pick In!", prompt="Jared, David, Aaron, Mike.\nWho will win? Enter Your Pick: ").lower()
is_race_on = True

jared = turtle.Turtle()
david = turtle.Turtle()
aaron = turtle.Turtle()
mike = turtle.Turtle()

jared.color('green')
david.color('blue')
aaron.color('orange')
mike.color('purple')

jared.penup()
david.penup()
aaron.penup()
mike.penup()


os.chdir(os.path.dirname(__file__))

screen.addshape(f"lordbiz.gif")
screen.bgpic(f"finish_line.gif")

jared.shape('turtle')
david.shape('turtle')
aaron.shape('turtle')
mike.shape('lordbiz.gif')


jared.setposition(-230, 75)
david.setposition(-230, 25)
aaron.setposition(-230,-25)
mike.setposition(-230, -75)


turtles = [jared,david,aaron,mike]
turtles_str = ['jared','david','aaron','mike']


while is_race_on:
    jared.forward(random.randint(0,10))
    david.forward(random.randint(0,10))
    aaron.forward(random.randint(0,10))
    mike.forward(random.randint(1,11))

    for turtle in turtles:
        if turtle.xcor() >= 250:
            is_race_on = False


print("")

if user_bet == 'mike':
    if turtle_in_lead(turtles,turtles_str) == 'mike':
        print("You guessed correctly. Lord Biz never loses..")
    else:
        print(f"Great guess. Unfortunately, {turtle_in_lead(turtles,turtles_str)} won the race somehow but still a great guess.")
elif turtle_in_lead(turtles,turtles_str) == 'mike':
    print(f"Never bet against Lord Biz...")
else:
    print(f"You guessed correctly. The winner of the race is {turtle_in_lead(turtles,turtles_str)}. (but still don't bet against Lord Biz)")



screen.exitonclick()


#things i could add: finish the race and then give the standings

#figure out how to handle ties.
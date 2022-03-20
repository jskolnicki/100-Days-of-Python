import pandas as pd
import turtle
import os


ALIGNMENT = 'center'
FONT = ("Courier", 10, 'bold')

os.chdir(os.path.dirname(__file__))

screen = turtle.Screen()

usa = turtle.Turtle()
usa.hideturtle()
usa.penup()

df = pd.read_csv("50_states.csv")


screen.addshape("blank_states_img.gif")
screen.bgpic("blank_states_img.gif")


game = True
correct_guesses = 0
states_guessed_correctly = []

while correct_guesses < 50:
    guess = screen.textinput(title= f"{correct_guesses}/50 States Guessed", prompt = "Enter a State Name: ")
    if guess == None:
        break
    else:
        guess = guess.title()
    if guess in df.state.to_list() and guess not in states_guessed_correctly:
        states_guessed_correctly.append(guess)
        state_info = df[df['state'] == guess]
        correct_guesses += 1
        usa.goto(int(state_info.x), int(state_info.y))
        usa.write(guess, False, align= ALIGNMENT, font= FONT)


states_remaining = {"States": []}
for i in df.state.to_list():
    if i not in states_guessed_correctly:
        states_remaining["States"].append(i)


states_remaining = pd.DataFrame(states_remaining)
states_remaining.to_csv("states_remaining.csv")
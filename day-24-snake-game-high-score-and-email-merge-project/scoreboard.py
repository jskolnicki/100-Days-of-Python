from turtle import Turtle
import time
import os

os.chdir(os.path.dirname(__file__))

scoreboard_position = 0,280



ALIGNMENT = 'center'
FONT = ("Courier", 12, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("my_high_score.txt") as file:
            high_score = int(file.read())
        self.highscore = high_score
        self.penup()
        self.hideturtle()
        self.setposition(scoreboard_position)
        self.write(f"Score = {self.score}  |  High Score = {self.highscore}", False, align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score

        self.write(f"Score = {self.score}  |  High Score = {self.highscore}", False, align= ALIGNMENT, font= FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font= FONT)
        with open(f"{currentDir}\\Day 24 - Snake Game High Score and Email Merge Project\\my_high_score.txt") as file:
            high_score = int(file.read())
        if self.score > high_score:
            with open(f"{currentDir}\\Day 24 - Snake Game High Score and Email Merge Project\\my_high_score.txt", 'w') as file:
                file.write(str(self.score))
        time.sleep(2.5)
        self.score = 0
        self.clear()
        self.goto(scoreboard_position)
        self.write(f"Score = {self.score}  |  High Score = {self.highscore}", False, align= ALIGNMENT, font= FONT)

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 12, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0,280)
        self.write(f"Score = {self.score}", False, align= ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", False, align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font= FONT)
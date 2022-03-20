from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, 'bold')

class Scoreboard(Turtle):
    def __init__(self, x_position):
        """Creates the score with the given X-position."""
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(x_position,260)
        self.write(f"{self.score}", False, align= ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", False, align= ALIGNMENT, font= FONT)

    def game_over(self, player1_score, player2_score):
        self.goto(0,0)
        if player1_score > player2_score:
            self.write("PLAYER 1 WINS", align = ALIGNMENT, font= FONT)
        if player2_score > player1_score:
            self.write("PLAYER 2 WINS", align = ALIGNMENT, font= FONT)

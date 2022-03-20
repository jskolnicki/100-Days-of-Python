from turtle import Turtle


ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setposition(0,260)
        self.write(f"Level: {self.level}", False, align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font= FONT)

    def find_positions(self):
        positions = []
        for segment in self.segments:
            positions.append(segment.pos())
        return positions

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, align= ALIGNMENT, font=FONT)
        
from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.create_paddle(side)

    def create_paddle(self, side):
        """Creates a paddle on the left or right side of the board. Must specify 'left' or 'right."""
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(5,1,1)
        self.speed('fastest')
        if side.lower() == 'left':
            self.setposition(-380, 0)
        if side.lower() == 'right':
            self.setposition(380,0)

    def move_up(self):
        if self.pos()[1] < 240:
            self.setposition(self.pos()[0], self.pos()[1]+20)

    def move_down(self):
        if self.pos()[1] > -240:
            self.setposition(self.pos()[0], self.pos()[1]-20)

    def reset(self):
        self.setposition(self.pos()[0], 0)
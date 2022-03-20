import turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = turtle.Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setposition(position)
            self.segments.append(new_segment)
            self.find_positions()

    def add_tail(self):
        new_segment = turtle.Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        self.new_tuple_x = self.segments[-1].pos()[0] - (self.segments[-2].pos()[0] - self.segments[-1].pos()[0])
        self.new_tuple_y = self.segments[-1].pos()[1] - (self.segments[-2].pos()[1] - self.segments[-1].pos()[1])
        new_segment.setposition((self.new_tuple_x, self.new_tuple_y))
        self.segments.append(new_segment)
    


    def move(self):
        for seg_num in reversed(range(1,len(self.segments))):
            self.segments[seg_num].setposition(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if round(self.head.pos()[1]) == round(self.segments[1].pos()[1]):
            self.head.setheading(UP)

    def move_right(self):
        if round(self.head.pos()[0]) == round(self.segments[1].pos()[0]):
            self.head.setheading(RIGHT)

    def move_left(self):
        if round(self.head.pos()[0]) == round(self.segments[1].pos()[0]):
            self.head.setheading(LEFT)

    def move_down(self):
        if round(self.head.pos()[1]) == round(self.segments[1].pos()[1]):
            self.head.setheading(DOWN)
        
    def find_positions(self):
        positions = []
        for position in self.segments:
            positions.append(position.pos())
        return positions

    def reset(self):
        for tail in self.segments:
            tail.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
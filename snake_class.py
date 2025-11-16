from turtle import Turtle,Screen
up=90
down=270
right=0
left=180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.segments = []
        self.starting_pos = [(0,-20),(0,0),(0,20)]
        self.create_snake()
        self.head=self.segments[0]
        self.distance=10
    def create_snake(self):
        for pos in self.starting_pos:
            part = Turtle("square")
            part.penup()
            part.color("white")
            part.goto(pos)
            self.segments.append(part)
    def add_snake(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        # add new segment at the position of the last one
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def move_forward(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.segments[0].forward(self.distance)
    def go_up(self):
        if self.head.heading() != down:
            self.segments[0].setheading(90)
    def go_down(self):
        if self.head.heading()!=up:
            self.segments[0].setheading(270)
    def go_right(self):
        if self.head.heading() != left:
             self.segments[0].setheading(0)
    def go_left(self):
        if self.head.heading() != right:
              self.segments[0].setheading(180)


from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        jim = Turtle("square")
        jim.color("white")
        jim.penup()
        jim.goto(position)
        self.segments.append(jim)

    def extend(self):
        # add tw garna tara, kun position ma add garna vanda --last position ma garna. So, LIST ma last position
        # indicate garna vanako LIST[-1] hoo. List paxi ko position() vanako xai method ho Turtle class ko.
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            # Here, x coordinate of last square is made equal to 2nd last x cor of square.
            new_y = self.segments[seg_index - 1].ycor()
            # Here, y coordinate of last square is made equal to 2nd last y cor of square.
            self.segments[seg_index].goto(new_x, new_y)
            # Then, hami tyo x rw y coordinate li last square ko x and y coordinate banaunxau.
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

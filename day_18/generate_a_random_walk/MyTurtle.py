from turtle import Turtle, Screen
from random import randint, choice
from day_18.hirst_painting.colorgram import MyColorgram


class MyTurtle(Turtle):
    directions_list = [0, 90, 180, 270]

    def __init__(self, random_move_distance=40):
        super().__init__()
        self.random_move_distance = random_move_distance
        self.coloring = MyColorgram(extract_num=100)

    def draw_dot(self):
        """
        draw 10x10 dots with random color extracted from color_list
        color_list (list of tuples): List of colors to be used for drawing dots.
        """
        self.hideturtle()
        self.coloring.append_color_tuple()
        if not self.coloring.color_list:
            raise ValueError("color_list cannot be empty")

        self.teleport(self.xcor() -250, self.ycor()-200)
        color_index = 0
        
        for row in range(10):
            starting_row_pos = self.pos()
            for col in range(10):
                current_color = self.coloring.color_list[color_index % len(self.coloring.color_list)]
                color_index += 1
                self.color(current_color)
                self.dot(size=20)
                self.teleport(self.xcor()+50, self.ycor())
            self.teleport(starting_row_pos[0], starting_row_pos[1]+50)

    def random_move(self, move_count=20):
        '''
        function: object moving
        parameters: Number of steps of moving
        '''
        self.speed(7)
        self.pen(pensize=10)
        self.error_exception(value=move_count, type=int)
        if move_count > 100:
            move_count = 100
        elif move_count < 0:
            move_count = 0

        self.screen.colormode(255)
        for _ in range(move_count):
            self.color_circling_turtle()
            direction = choice(self.directions_list)
            self.setheading(direction)
            self.forward(self.random_move_distance)

    def circling_circle(self, density):
        self.error_exception(value=density, type=int)
        if density < 1:
            density = 1
        elif density > 180:
            density = 180

        theta = 0
        while theta < 360:
            self.color_circling_turtle()
            self.speed(11)
            self.setheading(theta)
            self.circle(radius=-150)
            theta += density

    def error_exception(self, value, type):
        if not isinstance(value, type):
            raise ValueError(f"{value} must be an {type}")

    def color_circling_turtle(self):
        '''
        function: object coloring
        '''
        color_r = randint(0, 255)
        color_g = randint(0, 255)
        color_b = randint(0, 255)
        self.pencolor(color_r,color_g,color_b)

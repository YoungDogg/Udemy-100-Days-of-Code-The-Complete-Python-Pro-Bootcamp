from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1, 1)
        self.penup()
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10

        self.make_toss()

    def make_toss(self):
        new_pos = (self.xcor() + self.x_move, self.ycor() + self.y_move)
        self.goto(new_pos)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.accelerate()

    def reset(self):
        self.setpos(0,0)
        direction_xcor = 1
        if self.x_move < 0:
            direction_xcor = -1
        self.x_move = 10
        self.y_move = 10
        self.x_move *= -direction_xcor
        self.make_toss()

    def accelerate(self):
        speed = 1.125
        self.x_move *= speed
        self.y_move *= speed

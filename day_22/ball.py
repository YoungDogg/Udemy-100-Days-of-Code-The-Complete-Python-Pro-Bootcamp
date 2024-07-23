from turtle import Turtle


class Ball:
    def __init__(self, speed, size):
        self._ball = Turtle()
        self._ball.speed(speed)
        self._ball.shape("square")
        self._ball.shapesize(stretch_wid=size, stretch_len=size)
        self._ball.color("white")
        self._ball.penup()

    def initial_move(self):
        pos = self._ball.pos()
        self._ball.goto(pos[0]+self._ball.speed(), pos[1])

    def move(self, pos):
        # bounce from wall and paddles
        self._ball.pos(pos)
        self._ball.goto(pos[0], pos[1])

    def check_collision(self):
        # Determine if the ball has hit a paddle or the screen edges
        pass

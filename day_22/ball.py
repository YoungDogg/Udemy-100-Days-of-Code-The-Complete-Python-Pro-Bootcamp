from turtle import Turtle
import random


class Ball:
    def __init__(self, speed, size, screen):
        self._screen = screen
        self._ball = Turtle()
        self._ball.speed(10)
        self._ball.shape("square")
        self._ball.shapesize(stretch_wid=size, stretch_len=size)
        self._ball.color("white")
        self._ball.penup()
        self._dx = speed
        self._dy = 0
        self._is_moving = False

    @property
    def ball(self):
        return self._ball

    def initial_move(self):
        self._is_moving = True

    def reset_ball(self):
        self._ball.goto(0, 0)
        self._is_moving = False

    def move(self):
        if self._is_moving:
            # bounce from wall and paddles
            # if the ball hit the screen, make direction opposite
            new_x, new_y = self._ball.pos()
            new_x += self._dx
            new_y += self._dy
            self._ball.goto(new_x, new_y)

    def ball_distance(self, obj):
        return self.ball.distance(obj)

    def bounce_2_wall(self):
        print("ball bounces to wall")
        self._dy *= -1

    def bounce_2_paddle(self,paddle):
        # make both absolute value
        # turning x-coordinate direction
        self._dx *= -1
        # make random angle by adding random y-coordinate
        # test angles before implementing
        random_y = random.randint(-10,10) * 0.1
        # apply paddle's y-coordinate direction and speed
        # paddle_speed = paddle.speed()
        self._dy += random_y
        # apply more x-coordinate speed
        self._dx *= 1.2

from turtle import Turtle
from Screen import GameScreen
from typing import List
import time


class Snake:
    def __init__(self):
        self.snake: List[Turtle] = []
        self.snake_screen = GameScreen()
        x_pos = 0
        for _ in range(3):
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.shapesize(stretch_wid=1, stretch_len=1)
            segment.penup()
            segment.goto(x=x_pos, y=0)
            self.snake.append(segment)
            x_pos += -20
        self.head = self.snake[0]

    def move_snake(self, time_sleep: float = .1, speed: int = 10):
        for i in range(len(self.snake)-1,0,-1):
            [x_pos, y_pos] = self.snake[i-1].position()
            self.snake[i].goto(x=x_pos,y=y_pos)
        self.head.forward(speed)
        time.sleep(time_sleep)

    def turning_snake(self, time_sleep: float = .1):
        # TODO: insert key a,b, arrow left, arrow right
        if self.head.heading() != 90:
            self.head.setheading(90)

    def start_snake(self):
        # set snake
        # move snake while true
        while True:

        time.sleep(time_sleep)


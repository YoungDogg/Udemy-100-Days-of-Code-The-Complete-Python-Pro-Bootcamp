from turtle import Turtle
from Screen import GameScreen
from typing import List
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class Snake:
    def __init__(self):
        self.snake: List[Turtle] = []
        self.snake_screen = GameScreen().screen
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
        for i in range(len(self.snake) - 1, 0, -1):
            [x_pos, y_pos] = self.snake[i - 1].position()
            self.snake[i].goto(x=x_pos, y=y_pos)
        self.head.forward(speed)
        self.snake_screen.update()
        time.sleep(time_sleep)

    def turn_left(self):
        self.head.setheading(self.head.heading() + 90)
        logging.info("turn left")

    def turn_right(self):
        self.head.setheading(self.head.heading() - 90)
        logging.info('turn right')

    def start_snake(self):
        self.snake_screen.listen()
        self.snake_screen.onkey(self.turn_left, "Left")
        self.snake_screen.onkey(self.turn_left, "a")
        self.snake_screen.onkey(self.turn_left, "A")
        self.snake_screen.onkey(self.turn_right, "Right")
        self.snake_screen.onkey(self.turn_right, "d")
        self.snake_screen.onkey(self.turn_right, "D")
        while True:
            self.move_snake()

from turtle import Turtle
from screen import GameScreen
from typing import List
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class Snake:
    def __init__(self, screen):
        self._x_pos = 0
        self._y_pos = 0
        self._snake = []
        self._initial_length = 3
        self.snake_screen = screen
        self._initialize_snake(increment=self._initial_length)

    @property
    def snake(self):
        return self._snake

    @property
    def head(self):
        return self._snake[0]

    def _initialize_snake(self, increment: int):
        for _ in range(increment):
            self.extend_segment()
        self.head.color("blue")

    def extend_segment(self, increment: int = 1):
        for _ in range(increment):
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.shapesize(stretch_wid=1, stretch_len=1)
            segment.penup()
            segment.setpos(x=self._x_pos, y=self._y_pos)
            self._snake.append(segment)
            self.snake_screen.update()
            self._x_pos = self._snake[-1].xcor()
            self._y_pos = self._snake[-1].ycor()

    def append_score(self):
        # count scroe by segments
        score = len(self.snake) -self._initial_length

        return score
        pass

    def move_snake(self, speed: int = 10):
        for i in range(len(self._snake) - 1, 0, -1):
            self._x_pos, self._y_pos = self._snake[i - 1].position()
            self._snake[i].goto(x=self._x_pos, y=self._y_pos)
        self.head.forward(speed)

    def turn_left(self):
        self.head.setheading(self.head.heading() + 90)
        logging.info("turn left")

    def turn_right(self):
        self.head.setheading(self.head.heading() - 90)
        logging.info('turn right')

    def key_bound(self):
        self.snake_screen.listen()
        self.snake_screen.onkey(self.turn_left, "Left")
        self.snake_screen.onkey(self.turn_left, "a")
        self.snake_screen.onkey(self.turn_left, "A")
        self.snake_screen.onkey(self.turn_right, "Right")
        self.snake_screen.onkey(self.turn_right, "d")
        self.snake_screen.onkey(self.turn_right, "D")

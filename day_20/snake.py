from turtle import Turtle
from screen import GameScreen
from typing import List
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class Snake:
    def __init__(self, screen):
        self.x_pos = 0
        self.y_pos = 0

        self.snake: List[Turtle] = []
        self.snake_screen = screen
        self.extend_segment(increment=3)

        self.head = self.snake[0]
        self.head.color("blue")

    def extend_segment(self, increment: int = 1):

        for _ in range(increment):
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.shapesize(stretch_wid=1, stretch_len=1)
            segment.penup()
            segment.setpos(x=self.x_pos, y=self.y_pos)
            self.snake.append(segment)
            self.snake_screen.update()
            self.x_pos = self.snake[-1].xcor()
            self.y_pos = self.snake[-1].ycor()

    def move_snake(self, speed: int = 10):
        for i in range(len(self.snake) - 1, 0, -1):
            [self.x_pos, self.y_pos] = self.snake[i - 1].position()
            self.snake[i].goto(x=self.x_pos, y=self.y_pos)
        self.head.forward(speed)
        # self.snake_screen.update()

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

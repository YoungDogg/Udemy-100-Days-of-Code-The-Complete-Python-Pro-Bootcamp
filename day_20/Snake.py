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
            segment.penup()
            segment.goto(x=x_pos, y=0)
            self.snake.append(segment)
            x_pos += -20

    def idle_snake(self, time_sleep: float = .1,speed: int = 10):
        self.snake_screen.screen.update()
        time.sleep(time_sleep)
        for segment in self.snake:
            segment.forward(speed)

    # TODO:
    def turning_snake(self,time_sleep: float = .1,direction:str = "a",speed: int = 30):
        self.snake_screen.screen.update()
        time.sleep(time_sleep)
        count = 5
        while count > 0:
            for idx, segment in enumerate(self.snake):
                segment.setheading(90)
                segment.forward(speed)
                if idx+1 < len(self.snake):
                    for i,_ in enumerate(range(idx+1,len(self.snake))):
                        self.snake[i].forward(speed)
                print(f"idx: {idx}, i: {i}")


            count -= 1



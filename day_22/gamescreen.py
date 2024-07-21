from turtle import Screen
from tkinter import *


class GameScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._screen = Screen()
        self._screen.bgcolor("black")
        self._screen.title("Pong Game")
        self._screen.setup(width=self.width, height=self.height)
        print(f"Initialized screen size: ({self.width}, {self.height})")
        # self.screen.tracer(tracer)

    @property
    def screen(self):
        return self._screen

    @property
    def get_screen_size(self):
        return self.width, self.height

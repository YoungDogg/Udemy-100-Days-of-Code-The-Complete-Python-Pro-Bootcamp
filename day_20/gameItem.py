from screen import GameScreen
from turtle import Turtle
import random


class Item:
    def __init__(self, screen):
        self.screen = screen
        self.apple = self.create_apple()
        self.boundary = 30
        self._apple_pos = self.respawn()

    @staticmethod
    def create_apple():
        apple = Turtle()
        apple.color("pink")
        apple.shape("circle")
        apple.shapesize(1, 1)
        apple.penup()
        return apple

    @property
    def get_apple_pos(self):
        return self._apple_pos

    def respawn(self):
        self._apple_pos = self.get_apple_cor()
        self.apple.setpos(self._apple_pos)
        return self._apple_pos

    def get_apple_cor(self):
        left = int(-(self.screen.window_width() / 2) + self.boundary)
        right = int(self.screen.window_width() / 2 - self.boundary)
        top = int(self.screen.window_height() / 2 - self.boundary)
        bottom = int((-self.screen.window_height() / 2) + self.boundary)
        return random.randint(left, right), random.randint(bottom, top)

    def hide(self):
        self.apple.hideturtle()

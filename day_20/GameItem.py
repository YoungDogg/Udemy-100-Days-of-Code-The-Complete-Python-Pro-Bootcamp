from Screen import GameScreen
from turtle import Turtle
import random


class Item:
    def __init__(self):
        self.screen = GameScreen().screen
        self.s_width = self.screen.window_width()
        self.s_height = self.screen.window_height()
        # subtract apple size
        self.s_coordinate = {
            'left': -self.s_width / 2 + 20, 'right': self.s_width / 2 - 20,
            'top': self.s_height / 2 - 20, 'bottom': -self.s_height / 2 + 20
        }

        self.apple = Turtle()
        self.apple.color("pink")
        self.apple.shape("circle")
        self.apple.shapesize(1, 1)
        self.apple.penup()
        self.apple_pos = self.get_apple_cor()
        self.apple.setpos(self.apple_pos)
        # self.screen.update()

    def get_apple_cor(self):
        left = int(self.s_coordinate['left'])
        right = int(self.s_coordinate['right'])
        top = int(self.s_coordinate['top'])
        bottom = int(self.s_coordinate['bottom'])

        respawn_x = random.randint(left, right)
        respawn_y = random.randint(bottom, top)

        return respawn_x, respawn_y




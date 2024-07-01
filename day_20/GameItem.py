from Screen import GameScreen
from turtle import Turtle

class Item:
    def __init__(self):
        self.apple_list = []
        for _ in range(5):
            apple = Turtle()
            apple.color("pink")
            apple.shape("circle")
            apple.shapesize(1, 1)
            apple.setpos(0, 0)
            self.apple_list.append(apple)

        self.screen = GameScreen().screen
        self.s_width = self.screen.window_width()
        self.s_height = self.screen.window_height()
        # subtract apple size
        self.s_coordinate = {
            'left': -self.s_width / 2 + 20, 'right': self.s_width / 2 - 20,
            'top': self.s_height / 2 - 20, 'bottom': -self.s_height / 2 + 20
        }

        self.apple_list[0].setpos(self.s_coordinate['left'],self.s_coordinate['top'])
        self.apple_list[1].setpos(self.s_coordinate['right'], self.s_coordinate['top'])
        self.apple_list[2].setpos(self.s_coordinate['left'], self.s_coordinate['bottom'])
        self.apple_list[3].setpos(self.s_coordinate['right'], self.s_coordinate['bottom'])
        self.apple_list[4].setpos(0,0)

        self.screen.update()
        print(self.apple_list)

    def spawn_apple(self):
        # TODO: screen info


        # TODO: random pos
        pass


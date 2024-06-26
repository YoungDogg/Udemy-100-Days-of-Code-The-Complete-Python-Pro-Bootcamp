from Snake import Snake
from Screen import GameScreen


class GameCenter:
    def __init__(self, width, height):
        self.screen = GameScreen(width=width, height=height).screen
        self.snake = Snake()
        self.snake.turning_snake()
from Snake import Snake
from Screen import GameScreen
from GameItem import Item

class GameCenter:
    def __init__(self, width, height):
        self.screen = GameScreen(width=width, height=height).screen
        self.item = Item()
        self.item.spawn_apple()
        # self.snake = Snake()
        # self.snake.start_snake()


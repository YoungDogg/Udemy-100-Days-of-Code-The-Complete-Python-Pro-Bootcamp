from snake import Snake
from screen import GameScreen
from gameItem import Item
from gameCollision import GameCollision
import time


class GameCenter:
    def __init__(self, width, height):
        self.screen = GameScreen(width=width, height=height).screen
        self.snake = Snake(screen=self.screen)
        self.apple = Item(screen=self.screen)
        self.collision = GameCollision(screen=self.screen, snake=self.snake)

        self.start_game()
        self.screen.mainloop()

    def start_game(self):
        self.snake.key_bound()  # key bound
        is_over = False
        while not is_over:
            self.snake.move_snake()  # snake moving
            self.ate_apple()  # ate apple?
            is_over = self.collision.collision()  # collision
            self.screen.update()
            time.sleep(.1)

    def ate_apple(self):
        snake_x = int(self.snake.head.xcor())
        snake_y = int(self.snake.head.ycor())
        [apple_x, apple_y] = self.apple.apple_pos
        apple_cols_size = self.apple.apple.shapesize()[0] + 22
        if (apple_x - apple_cols_size <= snake_x <= apple_x + apple_cols_size) and (
                apple_y - apple_cols_size <= snake_y <= apple_y + apple_cols_size):
            # increment snake segment
            self.snake.extend_segment()
            # apple disappear
            self.apple.hide()
            # self.apple = None
            del self.apple
            # respawn other apple
            self.apple = Item(screen=self.screen)

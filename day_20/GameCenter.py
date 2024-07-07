from Snake import Snake
from Screen import GameScreen
from GameItem import Item
import time


class GameCenter:
    def __init__(self, width, height):
        self.screen = GameScreen(width=width, height=height).screen
        self.apple = Item()
        self.snake = Snake()

    def start_game(self):
        self.snake.key_bound()  # key bound
        is_over = False
        while not is_over:
            self.snake.move_snake()  # snake moving
            is_over = self.collision()  # collision
            self.screen.update()
            time.sleep(.1)

    # collision with screen, snake itself, item
    def collision(self):
        screen_x = self.screen.window_width()
        screen_y = self.screen.window_height()
        snake_x = int(self.snake.head.xcor())
        snake_y = int(self.snake.head.ycor())

        def collision_screen():
            if snake_x >= int(screen_x / 2) or snake_x <= -int(screen_x / 2):
                return True  # change this to game over

            if snake_y >= int(screen_y / 2) or snake_y <= -int(screen_y / 2):
                return True  # change this to game over

        def collision_apple():
            [apple_x, apple_y] = self.apple.apple_pos
            apple_size = self.apple.apple.shapesize()[0] + 22
            if (apple_x - apple_size <= snake_x <= apple_x + apple_size) and (
                    apple_y - apple_size <= snake_y <= apple_y + apple_size):
                return True

        def collision_snake():
            head = self.snake.head
            snake = self.snake.snake
            for idx in range(1, len(self.snake.snake)):
                if head.distance(snake[idx]) < snake[1].distance((snake[2].pos())) -1:
                    snake[idx].color("red")
                    return True
            return False

        if collision_screen() or collision_apple() or collision_snake():
            return True
        return False

from snake import Snake
from screen import GameScreen
from gameItem import Item


class GameCollision:
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake

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

        def collision_snake():
            head = self.snake.head
            snake = self.snake.snake
            for idx in range(1, len(snake)):
                if head.distance(snake[idx]) < snake[1].distance((snake[2].pos())) - 1:
                    snake[idx].color("red")
                    return True
            return False

        if collision_screen() or collision_snake():
            return True
        return False

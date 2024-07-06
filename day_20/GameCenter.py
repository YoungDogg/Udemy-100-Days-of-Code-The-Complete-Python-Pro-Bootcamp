from Snake import Snake
from Screen import GameScreen
from GameItem import Item


class GameCenter:
    def __init__(self, width, height):
        self.screen = GameScreen(width=width, height=height).screen
        # self.item = Item()
        self.snake = Snake()

    def start_game(self):
        self.snake.key_bound()  # key bound
        is_over = False
        while not is_over:
            self.snake.move_snake()  # snake moving
            is_over = self.collision()  # collision

    # collision with screen, snake itself, item
    def collision(self):
        # get screen info, constant
        screen_x = self.screen.window_width()
        screen_y = self.screen.window_height()

        # get snake cor, updated, while-loop required
        snake_x = int(self.snake.head.xcor())
        snake_y = int(self.snake.head.ycor())

        def collision_screen():
            # print(f"screen: ({screen_x}, {screen_y})"
            #       f"snake: ({snake_x}, {snake_y})")

            if snake_x >= int(screen_x / 2) or snake_x <= -int(screen_x / 2):
                # change this to game over
                print(f"collided with snake  ({snake_x}, {snake_y})")
                return True

            if snake_y >= int(screen_y / 2) or snake_y <= -int(screen_y / 2):
                # change this to game over
                print(f"collided with snake  ({snake_x}, {snake_y})")
                return True

        def collision_apple():
            pass

        def collision_snake():
            pass

        collision_screen()
        # if collision_screen() or collision_apple() or collision_snake():
        if collision_screen():
            return True
        return False

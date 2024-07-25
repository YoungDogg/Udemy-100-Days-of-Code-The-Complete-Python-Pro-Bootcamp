from turtle import Turtle


class Ball:
    def __init__(self, speed, size, screen):
        self._screen = screen
        self._ball = Turtle()
        self._ball.speed(10)
        self._ball.shape("square")
        self._ball.shapesize(stretch_wid=size, stretch_len=size)
        self._ball.color("white")
        self._ball.penup()
        self._dx = speed
        self._dy = 0
        self._is_moving = False

    def initial_move(self):
        self._is_moving = True

    def reset_ball(self):
        self._ball.goto(0, 0)
        self._is_moving = False

    def move(self):
        if self._is_moving:
            # bounce from wall and paddles
            # if the ball hit the screen, make direction opposite
            new_x,new_y = self._ball.pos()
            new_x += self._dx
            new_y += self._dy
            screen_x, screen_y = self._screen.get_screen_size
            # if hit the wall
            if new_y > screen_y/2 or new_y > -screen_y/2:
                self._dy *= -1
            # if hit the paddle multiply -1 to x
            self._ball.goto(new_x, new_y)
            print(f"ball pos ({new_x},{new_y})")

    def check_collision(self, paddle):
        # Determine if the ball has hit a paddle or the screen edges
        # x goes negative direction, y keeps its own direction
        if self._ball.distance(paddle.paddle) < 20:
            pass

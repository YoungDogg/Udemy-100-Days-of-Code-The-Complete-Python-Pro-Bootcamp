import turtle
from paddle import Paddle
from ball import Ball
import time


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor('black')
    screen.title('pong')
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()

    screen.listen()
    screen.onkeypress(fun=r_paddle.moveUp, key='Up')
    screen.onkeypress(fun=r_paddle.moveDown, key='Down')
    screen.onkeypress(fun=l_paddle.moveUp, key='w')
    screen.onkeypress(fun=l_paddle.moveDown, key='s')

    screen_top = screen.window_height() / 2
    screen_bottom = -screen.window_height() / 2

    is_game_over = False
    while not is_game_over:
        time.sleep(0.05)
        ball.make_toss()
        if ball.ycor() >= screen_top - 30 or ball.ycor() <= screen_bottom + 30:
            ball.bounce()

        screen.update()

    screen.exitonclick()


if __name__ == '__main__':
    main()

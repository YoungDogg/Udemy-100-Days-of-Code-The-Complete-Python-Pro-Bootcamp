import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

MARGIN_WIDTH = 50
MARGIN_HEIGHT = 20
DISTANCE_BALL_PADDLE = 55
DISTANCE_BALL_SCREEN = 10


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor('black')
    screen.title('pong')
    screen.tracer(0)

    screen_top = screen.window_height() / 2
    screen_bottom = -screen.window_height() / 2
    screen_half_width = screen.window_width() / 2

    r_paddle = Paddle((screen_half_width - MARGIN_WIDTH, 0))
    l_paddle = Paddle((-(screen_half_width - MARGIN_WIDTH), 0))
    ball = Ball()
    score = Scoreboard()

    screen.listen()
    screen.onkeypress(fun=r_paddle.moveUp, key='Up')
    screen.onkeypress(fun=r_paddle.moveDown, key='Down')
    screen.onkeypress(fun=l_paddle.moveUp, key='w')
    screen.onkeypress(fun=l_paddle.moveDown, key='s')

    is_game_over = False
    while not is_game_over:
        time.sleep(0.05)
        ball.make_toss()
        # detect collision with wall
        if (ball.ycor() >= screen_top - MARGIN_HEIGHT or
                ball.ycor() <= screen_bottom + MARGIN_HEIGHT):
            ball.bounce_wall()

        # detect collision with paddle
        # the ball checks 2 things: margin(MARGIN, y-axis) and paddle
        r_paddle_margin = screen_half_width - (MARGIN_WIDTH + 20)
        l_paddle_margin = -(screen_half_width - (MARGIN_WIDTH + 20))
        if ((ball.xcor() >= r_paddle_margin and ball.distance(r_paddle.pos()) < DISTANCE_BALL_PADDLE)
                or (ball.xcor() <= l_paddle_margin and ball.distance(l_paddle.pos()) < DISTANCE_BALL_PADDLE)):
            ball.bounce_paddle()

        # if the ball is out, reset and toss to other side
        if ball.xcor() > screen_half_width - DISTANCE_BALL_SCREEN:
            score.is_right_scored = True
            score.plus_one()
            ball.reset()
        elif ball.xcor() < - (screen_half_width - DISTANCE_BALL_SCREEN):
            score.is_right_scored = False
            score.plus_one()
            ball.reset()

        screen.update()

    screen.exitonclick()


if __name__ == '__main__':
    main()

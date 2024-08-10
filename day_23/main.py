from turtle import Screen
from character import GameTurtle
from car import Car
import time


def main():
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor('white')
    screen.tracer(0)

    screen.listen()
    turtle = GameTurtle(screen)
    difficulty = 1
    car = Car(screen, difficulty)

    is_game_over = False
    while not is_game_over:
        time.sleep(0.01)

        car.move_car()

        screen.update()
    screen.exitonclick()


if __name__ == '__main__':
    main()

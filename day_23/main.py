from turtle import Screen
from character import GameTurtle
from car import Car
from pack_of_cars import PackOfCars
import time


def main():
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor('white')
    screen.tracer(0)

    screen.listen()
    turtle = GameTurtle(screen)
    difficulty = 1

    cars = PackOfCars(screen, difficulty)
    cars.spawn_cars()

    is_game_over = False
    while not is_game_over:
        time.sleep(0.01)

        for car in cars.car_list:
            car.move_car()

        screen.update()
    screen.exitonclick()


if __name__ == '__main__':
    main()

from turtle import Screen, Turtle
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
    player = GameTurtle(screen)
    difficulty = 1

    cars = PackOfCars(screen, difficulty)

    display_level = Turtle()
    display_level.hideturtle()
    display_level.penup()
    display_level.goto(0, 250)

    is_game_over = False
    while not is_game_over:
        time.sleep(0.01)

        cars.manage_cars()

        # hit by the car
        for car in cars.car_list:
            if player.distance(car) < 22:
                player.color("red")
                is_game_over = True

        # stage clear
        if player.ycor() > (80 / 100) * (screen.window_height() / 2):
            difficulty += 1
            cars.difficulty = difficulty
            player.hideturtle()
            player = GameTurtle(screen)
            for idx, car in enumerate(cars.car_list):
                car.hideturtle()
            cars.car_list = []
            cars.spawn_cars()

        display_level.clear()
        display_level.write(difficulty, align='center', font=('Courier', 30, 'normal'))

        screen.update()
    # game over
    game_over_display = Turtle()
    game_over_display.hideturtle()
    game_over_display.penup()
    game_over_display.goto(0, 0)
    game_over_display.write("Game Over", align='center', font=('Courier', 60, 'normal'))
    # screen.update() # question: without this, how could the game over be displayed?

    screen.exitonclick()


if __name__ == '__main__':
    main()

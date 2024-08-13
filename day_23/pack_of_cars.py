import random

from car import Car

'''
manage pack of cars
keep spawning, disappearing them

put car objects on a list. 
Generate them by appending in the list.
Out of the screen, delete the car in the list.
Re-generate the car if the list is empty. <<<< this is collision thing
How to keep number of cars?
get how many cars on the screen
if the cars out of the screen, subtract the number(delete on the list later)


attribute: number of cars, current car num, 
method: keep number of cars on the screen
'''


class PackOfCars:
    def __init__(self, screen, difficulty):
        self.__screen = screen
        self.__difficulty = difficulty
        self.car_list = []
        self.num_of_cars = 5
        self.spawn_cars()

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, val: int):
        self.__difficulty += val

    def spawn_cars(self):
        for _ in range(self.num_of_cars + (self.__difficulty * 2)):
            self.car_list.append(Car(self.__screen, self.__difficulty))

    def manage_cars(self):
        scn_width = self.__screen.window_width() / 2
        for idx, car in enumerate(self.car_list):
            car.move_car()
            if not -scn_width < car.xcor() < scn_width:
                self.car_list.pop(idx)
                car.hideturtle()  # screen.clear() better for buffer managing
                self.car_list.append(Car(self.__screen, self.__difficulty))

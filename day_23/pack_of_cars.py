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

attribute: number of cars, current car num, 
method: keep number of cars on the screen
'''


class PackOfCars:
    def __init__(self, screen, difficulty):
        self.__screen = screen
        self.__difficulty = difficulty
        self.car_list = []
        # self.num_of_cars = 12 + difficulty
        self.num_of_cars = 10 + (difficulty * 2)

    def spawn_cars(self):
        for _ in range(self.num_of_cars):
            self.car_list.append(Car(self.__screen, self.__difficulty))

    def delete_cars(self, car):
        if car in self.car_list:
            car = None

    def check_car_out_screen(self):
        pass

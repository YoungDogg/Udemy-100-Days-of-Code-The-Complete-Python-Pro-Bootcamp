import math


class StateLocator:
    def __init__(self, screen, data, score):
        self.__data = data
        self.__score = score
        self.__screen = screen

    # get game screen coordinate by clicking
    def return_coordinates(self, x, y):
        clicked_coord = [x, y]
        self.find_closest_state(clicked_coord)

    # get the closest Euclidean distance and compare and return the smallest
    def find_closest_state(self, clicked_coord):
        closet_distance = 10 ** 9
        state_name = None
        for state in self.__data.coordinate_list:
            x = (clicked_coord[0] - int(state[0])) ** 2
            y = (clicked_coord[1] - int(state[1])) ** 2
            current_distance = float(f"{math.sqrt(x + y):.2f}")
            if current_distance < closet_distance:
                closet_distance = current_distance
                state_name = state[2]

        self.check_state(state_name)

    def check_state(self, state_name):
        # input popup
        input_return = self.__screen.textinput("Guess the State", "Name?")

        if not input_return or not input_return.isalpha():
            self.__screen.textinput("Error", "Invalid input! Please enter a valid state name (letters only)")
            return

        # condition comparing input and the state list
        if state_name.lower() == input_return.lower():
            # +1 score
            self.__score.increment_score()
            self.__score.display_ui_all()
        else:
            if self.__data.highest_score < self.__score.score:
                self.__data.highest_score = self.__score.score
                self.__data.save_score2file()
            self.__score.display_gameover()
            self.__screen.exitonclick()

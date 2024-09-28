class StateLocator:
    def __init__(self,screen, data):
        self.__data = data
        pass

    # get game screen coordinate by clicking
    @staticmethod
    def return_coordinates(x, y):
        clicked_coord = [x, y]
        find_closest_state(clicked_coord)

    # get the closest Euclidean distance and compare and return the smallest
    @staticmethod
    def find_closest_state(clicked_coord):
        closet_distance = 10 ** 9
        for state in self.__data.coordinate_list:
            x = (clicked_coord[0] - int(state[0])) ** 2
            y = (clicked_coord[1] - int(state[1])) ** 2
            current_distance = float(f"{math.sqrt(x + y):.2f}")
            if current_distance < closet_distance:
                closet_distance = current_distance
                state_name = state[2]

        check_state(state_name)

    @staticmethod
    def check_state(state_name):
        # input popup
        input_return = screen.textinput("Guess the State", "Name?")
        print(f"state_name: {state_name} input_return: {input_return}")
        # condition comparing input and the state list
        if state_name.lower() == input_return.lower():
            # +1 score
            self.__data.score
            self.__data.score += 1

            display_ui(score_ui2, screen, "score: ", 50, 70)
            display_ui(score_ui, screen, self.__data.score, 62, 70)
            display_ui(highest_score_ui, screen, "highest: ", 50, 80)
            display_ui(highest_score_ui2, screen, self.__data.highest_score, 62, 80)
        else:
            save_score2file(self.__data.score_data)

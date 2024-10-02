import pandas as pd
import os.path


class Data:
    def __init__(self):
        self.__data = pd.read_csv("50_states.csv")
        self.__score_data = None
        self.__score_dict = None
        self.init_save_file()

    @property
    def highest_score(self):
        return self.__score_data.loc[0, "highest"]

    @highest_score.setter
    def highest_score(self, val: int):
        self.__score_data.loc[0, "highest"] = val

    # get coordinate data list
    @property
    def coordinate_list(self):
        return [list(coord) for coord in zip(self.__data["x"], self.__data["y"], self.__data["state"])]

    def init_save_file(self):
        file_name = 'scoreboard.csv'
        if not os.path.exists(file_name):
            self.__score_dict = {"highest": 0}
            self.__score_data = pd.DataFrame([score_dict])
            self.__score_data.to_csv("scoreboard.csv", index=True)
        else:
            # if there's a csv file already
            self.__score_data = pd.read_csv(file_name)

    def save_score2file(self):
        self.__score_data.to_csv("scoreboard.csv", index=False)

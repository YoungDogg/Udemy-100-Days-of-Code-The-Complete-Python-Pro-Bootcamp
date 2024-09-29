import os.path

import pandas
import pandas as pd

from singleton import GlobalValue
import turtle


class Score:
    def __init__(self, screen):
        self.__screen = screen
        self.__data = pandas.read_csv("50_states.csv")
        self.__score_data = None
        self.init_save_file()
        self.__score = GlobalValue().value
        self.__score_ui = self.generate_UI_obj()
        self.__score_ui2 = self.generate_UI_obj()
        self.__highest_score_ui = self.generate_UI_obj()
        self.__highest_score_ui2 = self.generate_UI_obj()
        self.__gameover_ui = self.generate_UI_obj()

    @property
    def score_data(self):
        return self.__score_data

    @property
    def highest_score(self):
        return self.__score_data.loc[0, "highest"]

    # get coordinate data list
    @property
    def coordinate_list(self):
        return [list(coord) for coord in zip(self.__data["x"], self.__data["y"], self.__data["state"])]

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val: int):
        self.__score = val

    def init_save_file(self):
        file_name = 'scoreboard.csv'
        if not os.path.exists(file_name):
            score_dict = {"highest": 0}
            self.__score_data = pandas.DataFrame([score_dict])
            self.__score_data.to_csv("scoreboard.csv", index=True)
        else:
            # if there's a csv file already
            self.__score_data = pd.read_csv(file_name)

    def increment_score(self):
        # self.__score += 1 # this worked normal
        self.score += 1 # this incremented drastically


    # make the score
    # UI
    @staticmethod
    def generate_UI_obj():
        ui_obj = turtle.Turtle()
        ui_obj.hideturtle()
        ui_obj.penup()
        ui_obj.speed(10)
        return ui_obj

    def save_score2file(self):
        if self.__score_data.loc[0, "highest"] < self.__score:
            self.__score_data.loc[0, "highest"] = self.__score
            self.__score_data.to_csv("scoreboard.csv", index=False)

    def display_ui_all(self):
        self.display_ui(self.__score_ui2, "score: ", 50, 70)
        self.display_ui(self.__score_ui, self.score, 62, 70)
        self.display_ui(self.__highest_score_ui, "highest: ", 45, 80)
        self.display_ui(self.__highest_score_ui2, self.highest_score, 62, 80)

    def display_ui(self, ui_obj, text, width, height, x0y0=False):
        ui_obj_width = (self.__screen.window_width() / 2) * width / 100
        ui_obj_height = (self.__screen.window_height() / 2) * height / 100
        ui_obj.clear()
        if not x0y0:
            ui_obj.goto(ui_obj_width, ui_obj_height)
            ui_obj.write(text, align="left", font=('Arial', 12, 'bold'))
        else:
            ui_obj.write(text, align="center", font=('Arial', 36, 'bold'))

    def display_gameover(self):
        self.display_ui(self.__gameover_ui, "game over", 0, 0, True)

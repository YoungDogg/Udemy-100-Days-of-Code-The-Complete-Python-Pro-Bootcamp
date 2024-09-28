import pandas
from singleton import GlobalValue


class Score:
    def __init__(self):
        self.__data = pandas.read_csv("50_states.csv")
        self.__score_dict = {"highest": 0}
        self.__score_data = pandas.DataFrame([self.__score_dict])
        self.__score = GlobalValue().value

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

    # make the score
    # UI
    @staticmethod
    def generate_UI_obj():
        score_ui = turtle.Turtle()
        score_ui.hideturtle()
        score_ui.penup()
        score_ui.speed(10)
        return score_ui

    score_ui = generate_UI_obj()
    score_ui2 = generate_UI_obj()

    highest_score_ui = generate_UI_obj()
    highest_score_ui2 = generate_UI_obj()

    @staticmethod
    def display_ui(score_ui, screen, text, width, height):
        score_ui_width = (screen.window_width() / 2) * width / 100
        score_ui_height = (screen.window_height() / 2) * height / 100
        score_ui.goto(score_ui_width, score_ui_height)
        score_ui.clear()
        score_ui.write(text, align="left", font=('Arial', 12, 'bold'))

    @staticmethod
    def save_score2file(score_data):
        self.__score
        highest = score_data.loc[0, "highest"]
        if self.__score > highest:
            score_data.loc[0, "highest"] = self.__score
            score_data.to_csv("scoreboard.csv", index=False)
